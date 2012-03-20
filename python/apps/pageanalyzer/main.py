import sys
import configparser
import urllib

USAGE = """USAGE:
$ python main.py -url page-url [-delay delay-time|]
    -url: the start url
    -delay: the delay between requests in milliseconds
"""

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
    print(url, delay)
