
class Graph:

    def __init__(self):
        self.vertices = {}
        self.edges = {}

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

    def add_edge(self, start_vertex, end_vertex, label=None, value=None):
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

    def get_neighbors(self):
        pass

    def get_edges(self):
        pass

class Edge:

    def __init__(self, start_vertex, target_vertex, label=None, value=None):
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        self.label = ''
        self.vallue = 0
        if label:
            self.label = label
        if value:
            self.value = value

    def get_vertices(self):
        return self.start_vertex, self.target_vertex

if __name__ == '__main__':
    pass
