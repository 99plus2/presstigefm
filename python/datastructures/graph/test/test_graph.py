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

if __name__ == '__main__':
    unittest.main()
