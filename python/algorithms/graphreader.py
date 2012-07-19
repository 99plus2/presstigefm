"""
graphreader provides methods to parse a text file to a graph-object.
"""
import sys
sys.path.append('../datastructures/graph')
from graph import Graph

def txt_to_graph(filepath):
    graph = Graph()
    with open(filepath) as f:
        for line in f:
            tokens = line.replace('\n', '').split(' ')
            if tokens[0] == 'v':
                graph.add_vertex(tokens[1])
            elif tokens[0] == 'e':
                graph.add_edge(tokens[1], tokens[2])

if __name__ == '__main__':
    print('hello')
