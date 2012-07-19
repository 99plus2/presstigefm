"""
This file contains a implementation of the TOPSORT algorithm to obtain a
topological order of a directed acyclic graph.
"""
import sys
from graphreader import txt_to_graph

def topsort(graph):
    """ Returns the topological order of the graph as a list. 
        graph = [datastructures.graph.Graph]
        returns [list(datastructures.graph.Vertex)], topological order of the graph """
    sorted_elements = []
    vertices_without_inedges = get_vertices_without_inedges(graph)
    while vertices_without_inedges:
        vertex = vertices_without_inedges.pop()
        sorted_elements.append(vertex)
        for successor in vertex.get_successors():
            graph.remove_edge_between(vertex, successor)
            if not successor.get_predecessors():
                vertices_without_inedges.append(successor)
    if graph.edges:
        print('Cycle detected in graph')
    return sorted_elements

def get_vertices_without_inedges(graph):
    """ Searches for vertices without a incoming edge.
        returns [list(datastructures.graph.Vertex)] """
    candidates = graph.vertices.copy()
    for edge in graph.edges:
        if edge.target_vertex.name in candidates:
            candidates.pop(edge.target_vertex.name)
    return [candidates[key] for key in candidates.keys()]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        graph = txt_to_graph(sys.argv[1])
        topological_order = topsort(graph)
        print(topological_order)
