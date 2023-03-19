class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


def kruskalsAlgorithm(edges):
    edges_list = []
    for i in range(len(edges)):
        for edge in edges[i]:
            edges_list.append([i, edge[0], edge[1]])

    sorted_list = sorted(edges_list, key=lambda x: x[2])

    no_of_vertices = len(edges)
    vertices = [i for i in range(no_of_vertices)]
    parent = {}

    for v in vertices:
        parent[v] = v
    ds = DisjointSet(vertices, parent)
    count = 0
    retlis = [[] for i in range(no_of_vertices)]
    for edge in sorted_list:
        print(edge)
        if count == no_of_vertices - 1:
            break
        if ds.find(edge[0]) != ds.find(edge[1]):
            A = edge[0]
            B = edge[1]
            retlis[A].append([B, edge[2]])
            retlis[B].append([A, edge[2]])
            ds.union(edge[0], edge[1])
            count += 1
    return retlis