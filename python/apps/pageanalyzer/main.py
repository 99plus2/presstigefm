import sys
import configparser
from urllib.request import urlopen
from urllib.parse import urlparse
import time
from bs4 import BeautifulSoup

USAGE = """USAGE:
$ python main.py -url page-url [-delay delay-time|]
    -url: the start url
    -delay: the delay between requests in seconds
"""

def scan_page(url, delay):
    queue = [url]
    visited = set()
    links = {}
    base_url = urlparse(url).hostname
    while queue:
        current_url = queue[0]
        queue = queue[1:]
        visited.add(current_url)
        if current_url not in links:
            links[current_url] = []
        html = urlopen(current_url).read()
        soup = BeautifulSoup(html)
        for link in soup.find_all('a'):
            link = link.get('href')
            if link and link.startswith('/'):
                link = 'http://' + base_url + link
            links[current_url].append(link)
            if urlparse(link).hostname == base_url and link not in visited:
                queue.append(link)
    print(links)
    return links

def parse_to_graph(links):
    pass

def generate_file(graph, filename):
    pass

def parse_arguments(argv):
    url = None
    delay = None
    try:
        for arg in argv:
            if arg == '-url':
                url = argv[argv.index(arg) + 1]
            elif arg == '-delay':
                delay = int(argv[argv.index(arg) + 1])
        if not url:
            raise Exception
        if not delay:
            delay = 0
    except:
        print(USAGE)
        sys.exit(0)

    return url, delay

if __name__ == '__main__':
    config = configparser.ConfigParser()
    try:
        config.read('config.cfg')
    except:
        print(USAGE)
    url, delay = parse_arguments(sys.argv)
    links = scan_page(url, delay)
    graph = parse_to_graph(links)
    generate_file(graph, 'graph.png')
