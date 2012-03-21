import unittest
from disjointset import DisjointSet, Node

class DisjointSetTest(unittest.TestCase):

    def test_all(self):
        disjoint_set = DisjointSet()
        x = Node()
        disjoint_set.makeset(x)
        self.assertEqual(x, x.parent)
        self.assertEqual(0, x.rank)

        y = Node()
        disjoint_set.makeset(y)
        disjoint_set.link(x, y)
        self.assertEqual(y, x.parent)
        self.assertEqual(y, y.parent)
        self.assertEqual(1, y.rank)
        self.assertEqual(0, x.rank)

if __name__ == '__main__':
    unittest.main()
