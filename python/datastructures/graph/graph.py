
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
            raise ValueError('vertex not in graph')

    def add_vertex(self, vertex_or_name):
        """ Adds a new Vertex into the graph. 
            Throws exception if vertex or name already in graph. """
        if isinstance(vertex_or_name, Vertex):
            if vertex_or_name.name in self.vertices:
                raise ValueError('name already exists in graph')
            self.vertices[vertex_or_name.name] = vertex_or_name
        else:
            if vertex_or_name in self.vertices:
                raise ValueError('can not insert same vertex twice')
            vertex = Vertex(name=vertex_or_name)
            self.vertices[vertex_or_name] = vertex

    def remove_vertex(self, vertex_or_name):
        pass

    def add_edge(self, start_vertex, end_vertex, label=None, value=None):
        """ Adds a edge between two vertices. Vertices can either be a
            Vertex-object or a id. Either way, they have to be already added.
            Returns the created edge. """
        _start_vertex = self.get_vertex(start_vertex)
        _end_vertex = self.get_vertex(end_vertex)

        edge = Edge(_start_vertex, _end_vertex, label, value)
        self.edges.append(edge)

        _start_vertex.add_neighbor(_end_vertex)
        _end_vertex.add_neighbor(_start_vertex)

        return edge

    def remove_edge(self, edge):
        pass

    def remove_edge(self, vertex1, vertex2):
        pass

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

    def add_neighbor(self, vertex):
        self.neighbors.append(vertex)

    def remove_neighbor(self, vertex):
        self.neighbors.remove(vertex)

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
