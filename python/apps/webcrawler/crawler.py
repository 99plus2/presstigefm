import sys
import urllib.request as request
import urllib.robotparser as robotparser
import time
import lxml.html
from lxml.etree import XMLSyntaxError

USAGE = """
>python crawler.py url [num_pages|]
\t url - the url to start the crawling
\t num_pages - the number of distinct pages to crawl before stopping the crawler
"""

class Crawler:

    TIME_BETWEEN_REQUESTS = 0.5 # the minimum time between a request on the same host

    def __init__(self, start_url):
        """ start_url = [ParseResult], the url to start crawling """
        self.start_url = start_url
        self.url_queue = [] 
        self.visited_pages = set()
        self.robot_parser = {}
        self.host_requests = {} # Saves the last time for a request on a domain
        self.visited = 0

    def start(self, num_pages):
        """ Starts the crawling. 
            num_pages = [int] > 0, the maximum number of pages until crawler stops """
        print('starting crawler with {0} and max. pages set to {1}'.format(self.start_url.geturl(), 
            num_pages))
        self.url_queue.append(self.start_url)
        start_time = time.time()
        while self.visited < num_pages and len(self.url_queue) > 0:
            current_url = self.url_queue.pop(0)
            print('processing {0}/{1}: {2}'.format(self.visited, num_pages, current_url.geturl()))
            if current_url.netloc in self.host_requests and \
                    time.time() - self.host_requests[current_url.netloc] < Crawler.TIME_BETWEEN_REQUESTS:
                self.url_queue.append(current_url)
            else:
                try:
                    links = self.gather_hyperlinks(current_url)
                    self.visited_pages.add(current_url.geturl())
                    self.add_links(links)
                    self.visited += 1
                except:
                    pass
        print('finished crawling in {0} seconds'.format(time.time() - start_time))

    def add_links(self, links):
        """ Adds all links which are allowed according to robots.txt and are not
            already visited to the url_queue.
            links = [list(ParseResult)], the list of urls to check and add """
        for link in links:
            if link.geturl() not in self.visited_pages and self.robot_allows(link):
                self.url_queue.append(link)

    def robot_allows(self, link):
        """ Checks if a link is allowed according to the page robots.txt.
            link = [ParseResult], the link to check
            return [bool], true if allowed - false otherwise """
        if not link.netloc in self.robot_parser:
            parser = robotparser.RobotFileParser()
            parser.set_url(link.geturl())
            try:
                parser.read()
                self.robot_parser[link.netloc] = parser
            except IOError as err:
                print(link.geturl() + ': ' + repr(err))
                return False
            except:
                return False
        return self.robot_parser[link.netloc].can_fetch('*', link.geturl())

    def gather_hyperlinks(self, url):
        """ Opens a url and searches its content for hyperlinks. 
            url = [ParseResult], the url to open and read
            returns [list(ParseResult)] list of found hyperlinks """
        links = []
        with request.urlopen(url.geturl()) as page:
            dom = lxml.html.fromstring(page.read().decode('utf-8'))
            self.host_requests[url.netloc] = time.time()
            for link in dom.xpath('//a/@href'):
                new_link = request.urlparse(link)
                if not new_link.scheme:
                    new_link = request.urlparse(url.scheme + '://' + url.netloc + new_link.path)
                if new_link.scheme == 'http':
                    links.append(new_link)
        return links


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(0)
    url = request.urlparse(sys.argv[1])
    num_pages = 1000 # default value
    if len(sys.argv) > 2:
        num_pages = int(sys.argv[2])
        if num_pages < 1:
            sys.exit('Number must be greater than 1')
    if url.netloc and url.scheme == 'http':
        crawler = Crawler(url)
        crawler.start(1000)
