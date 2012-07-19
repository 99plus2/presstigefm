"""
This file contains a implementation of the TOPSORT algorithm to obtain a
topological order of a directed acyclic graph.
"""
import sys
from graphreader import txt_to_graph

def topsort(graph):
    """ Returns the topological order of the graph as a list. """
    pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        graph = txt_to_graph(sys.argv[1])
        topological_order = topsort(graph)
        print(topological_order)
