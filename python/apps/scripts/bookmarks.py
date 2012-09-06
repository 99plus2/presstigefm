#!/usr/bin/python3
""" Little script to allow bookmarks paths in linux terminal. 
    Installation: 
        add to ~/.bashrc:
        function to()
        {
            cd `python3 [path-of-script]/bookmarks.py -to $1`;
        }
        alias bm="python3 [path-of-script]/bookmarks.py -bm $1"
"""
import sys
import os
import configparser

CONFIG_FILE = os.path.join(sys.path[0], 'bookmarks.txt')
CONFIG_FILE_TEMPLATE = """
[bookmarks]
"""
BOOKMARK_SECTION = 'bookmarks'

def set_bookmark(name, directory):
    """ Stores a new bookmark under given name to the directory. 
        name = string, the name of the bookmark
        directory = string, the directory to store as a bookmark """
    print('storing directory "{1}" as bookmark under name "{0}"'.format(name, directory))
    config = configparser.ConfigParser()
    config.readfp(open(CONFIG_FILE))
    config.set(BOOKMARK_SECTION, name, directory)
    config.write(open(CONFIG_FILE, 'w'))

def get_bookmark(name):
    """ Retrieves a bookmark under given name. If bookmark does not exists
        method returns '.'.
        name = string, the name of the bookmark """
    config = configparser.ConfigParser()
    config.readfp(open(CONFIG_FILE))
    return config.get(BOOKMARK_SECTION, name) if config.has_option(BOOKMARK_SECTION, name) else '.'

if __name__ == '__main__':
    # create new config file if non exists
    if not os.path.isfile(CONFIG_FILE):
        cfg_file = open(CONFIG_FILE, 'w')
        cfg_file.write(CONFIG_FILE_TEMPLATE)
        cfg_file.close()

    if '-bm' in sys.argv:
        bookmark_name = 'temp'
        if sys.argv.index('-bm') + 1 < len(sys.argv):
            bookmark_name = sys.argv[sys.argv.index('-bm') + 1]
        set_bookmark(bookmark_name, os.getcwd())
    elif '-to' in sys.argv:
        bookmark_name = 'temp'
        if sys.argv.index('-to') + 1 < len(sys.argv):
            bookmark_name = sys.argv[sys.argv.index('-to') + 1]
        print(get_bookmark(bookmark_name))
