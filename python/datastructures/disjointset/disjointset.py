"""
A disjoint set data structure maintains a collection of disjoint dynamic sets
over some ground set. Each set is identified by a representativ, which is some
member of the set.
"""

class DisjointSet:

    def makeset(self, x):
        x.parent = x
        x.rank = 0

    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.link(self.find(x), self.find(y))

    def link(self, x, y):
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
        if x.rank == y.rank:
            y.rank += 1

    def find(self, x):
        if x != x.parent:
            x.parent = self.find(x.parent)
        return x.parent

class Node:

    def __init__(self):
        self.parent = None
        self.rank = 0
