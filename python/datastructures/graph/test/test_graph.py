import unittest
import sys
sys.path.append('../')
from graph.graph import Graph, Vertex

class GraphTest(unittest.TestCase):

    def test_get_vertex(self):
        g = Graph()
        vertex = g.add_vertex('v1')

        self.assertEqual(vertex, g.get_vertex('v1'))
        self.assertEqual(vertex, g.get_vertex(vertex))
        self.assertRaises(ValueError, g.get_vertex, 'v2')

    def test_add_vertex(self):
        g = Graph()
        g.add_vertex('v1')
        self.assertEqual(1, len(g.vertices))
        self.assertRaises(ValueError, g.add_vertex, 'v1')

        vertex = Vertex('v2')
        g.add_vertex(vertex)
        self.assertEqual(2, len(g.vertices))
        self.assertRaises(ValueError, g.add_vertex, vertex)

    def test_add_edge(self):
        g = Graph()
        g.add_vertex('v1')
        g.add_vertex('v2')
        g.add_vertex('v3')
        g.add_vertex('v4')

        edge = g.add_edge('v1', 'v2')
        self.assertEqual(1, len(g.edges))
        self.assertEqual(1, len(g.get_vertex('v1').neighbors))
        self.assertEqual(1, len(g.get_vertex('v2').neighbors))
        self.assertTrue(g.get_vertex('v1') in edge.get_vertices())
        self.assertTrue(g.get_vertex('v2') in edge.get_vertices())

        edge = g.add_edge('v3', 'v4', label='foo', value=10)
        self.assertEqual('foo', edge.label)
        self.assertEqual(10, edge.value)

    def test_remove_vertex(self):
        g = Graph()
        vertex1 = g.add_vertex('v1')
        vertex2 = g.add_vertex('v2')
        g.add_vertex('v3')
        edge1 = g.add_edge('v1', 'v2')
        edge2 = g.add_edge('v1', 'v3')
        edge3 = g.add_edge('v2', 'v3')

        g.remove_vertex('v3')
        self.assertEqual(2, len(g.vertices))
        self.assertEqual(1, len(g.edges))
        self.assertTrue('v3' not in g.vertices)
        self.assertEqual(1, len(vertex1.neighbors))
        self.assertEqual(1, len(vertex2.neighbors))

    def test_remove_edge(self):
        g = Graph()
        vertex1 = g.add_vertex('v1')
        vertex2 = g.add_vertex('v2')
        vertex3 = g.add_vertex('v3')
        edge1 = g.add_edge(vertex1, vertex2)
        edge2 = g.add_edge(vertex2, vertex3)

        g.remove_edge(edge1)
        self.assertEqual(1, len(g.edges))
        self.assertTrue(edge1 not in g.edges)
        self.assertTrue(vertex2 not in vertex1.neighbors)

        g.remove_edge_between('v2', vertex3)
        self.assertEqual(0, len(g.edges))
        self.assertTrue(edge2 not in g.edges)
        self.assertTrue(vertex3 not in vertex2.neighbors)

if __name__ == '__main__':
    unittest.main()
