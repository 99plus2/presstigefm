import unittest
import sys
sys.path.append('../')
from graph.graph import Graph, Vertex

class GraphTest(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
