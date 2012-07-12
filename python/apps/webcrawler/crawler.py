import sys
import urllib.request as request
import lxml.html

USAGE = """
>python crawler.py url [num_pages|]
\t url - the url to start the crawling
\t num_pages - the number of distinct pages to crawl before stopping the crawler
"""

class Crawler:

    def __init__(self, start_url):
        """ start_url = [ParseResult], the url to start crawling """
        self.start_url = start_url

    def start(self, num_pages):
        """ Starts the crawling. 
        num_pages = [int] > 0, the maximum number of pages until crawler stops """
        print('starting crawler with {0} and max. pages set to {1}'.format(self.start_url.geturl(), 
            num_pages))
        print(len(self.gather_hyperlinks(self.start_url)))

    def gather_hyperlinks(self, url):
        """ Opens a url and searches its content for hyperlinks. 
        url = [ParseResult], the url to open and read
        returns [list(ParseResult)] list of found hyperlinks """
        links = []
        with request.urlopen(url.geturl()) as page:
            dom = lxml.html.fromstring(page.read().decode('utf-8'))
            for link in dom.xpath('//a/@href'):
                new_link = request.urlparse(link)
                if not new_link.netloc:
                    new_link = request.urlparse(url.scheme + '://' + url.netloc + new_link.path)
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
