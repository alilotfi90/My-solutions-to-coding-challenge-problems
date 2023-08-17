from typing import List


class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


def umbristan(n: int, breaks: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    dsu = UnionFind()
    breaks.reverse()
    n_components = n
    ret = []
    for x, y in breaks:
        ret.append(n_components)
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            n_components -= 1

    return ret[::-1]











