
class Graph:

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def get_vertex(self, vertex_or_name):
        """ Returns vertex or ValueError if vertex not in graph. """
        if isinstance(vertex_or_name, Vertex) and vertex_or_name.name in self.vertices:
            return vertex_or_name
        elif vertex_or_name in self.vertices:
            return self.vertices[vertex_or_name]
        else:
            raise ValueError('vertex not in graph: ' + vertex_or_name)

    def add_vertex(self, vertex_or_name):
        """ Adds a new Vertex into the graph. 
            Throws exception if vertex or name already in graph.
            Returns the added vertex. """
        if isinstance(vertex_or_name, Vertex):
            if vertex_or_name.name in self.vertices:
                raise ValueError('name already exists in graph')
            self.vertices[vertex_or_name.name] = vertex_or_name
            return vertex_or_name
        else:
            if vertex_or_name in self.vertices:
                raise ValueError('can not insert same vertex twice')
            vertex = Vertex(name=vertex_or_name)
            self.vertices[vertex_or_name] = vertex
            return vertex

    def remove_vertex(self, vertex_or_name):
        """ Removes a vertex from the graph and deletes it's incident edges. """
        vertex = self.get_vertex(vertex_or_name)
        vertex = self.vertices.pop(vertex.name)
        edges_to_remove = []
        for edge in self.edges:
            v1, v2 = edge.get_vertices()
            if vertex in (v1, v2):
                edges_to_remove.append(edge)
                if vertex == v1:
                    v2.remove_neighbor(vertex)
                else:
                    v1.remove_neighbor(vertex)
        for edge in edges_to_remove:
            self.edges.remove(edge)

    def add_edge(self, start_vertex, end_vertex, label=None, value=None):
        """ Adds a edge between two vertices. Vertices can either be a
            Vertex-object or a id. Either way, they have to be already added.
            Returns the created edge. """
        _start_vertex = self.get_vertex(start_vertex)
        _end_vertex = self.get_vertex(end_vertex)

        edge = Edge(_start_vertex, _end_vertex, label, value)
        self.edges.append(edge)

        _start_vertex.add_neighbor(edge)
        _end_vertex.add_neighbor(edge)

        return edge

    def remove_edge(self, edge):
        self.edges.remove(edge)
        v1, v2 = edge.get_vertices()
        v1.remove_neighbor(v2)
        v2.remove_neighbor(v1)

    def remove_edge_between(self, vertex1, vertex2):
        v1 = self.get_vertex(vertex1)
        v2 = self.get_vertex(vertex2)
        edge_to_remove = None
        for edge in self.edges:
            if v1 in edge.get_vertices() and v2 in edge.get_vertices():
                edge_to_remove = edge
                break
        self.edges.remove(edge_to_remove)
        v1.remove_neighbor(v2)
        v2.remove_neighbor(v1)

class Vertex:

    ID = 0

    def __init__(self, name=None, label=None):
        """ Creates a vertex with or without name and label. name attribute
            have to be unique. If no name is provided, constructor assigns
            internal ID as name. """
        self.name = Vertex.ID
        Vertex.ID += 1
        self.label = label or ''
        self.name = name or Vertex.ID
        self.neighbors = []
        self.edges = {}

    def add_neighbor(self, edge):
        vertex = edge.start_vertex
        if edge.start_vertex == self:
            vertex = edge.target_vertex
        self.neighbors.append(vertex)
        self.edges[vertex] = edge

    def remove_neighbor(self, vertex):
        self.neighbors.remove(vertex)
        self.edges.pop(vertex)

    def __repr__(self):
        s = '<Vertex> ' + repr(self.name)
        if self.label:
            s += ' [{0}]'.format(self.label)
        return s

class Edge:

    def __init__(self, start_vertex, target_vertex, label=None, value=None):
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        self.label = label or ''
        self.value = value or 0

    def get_vertices(self):
        return self.start_vertex, self.target_vertex

if __name__ == '__main__':
    pass
