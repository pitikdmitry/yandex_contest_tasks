"""
Build graph of substrings of texts
For every word:
1) word S=s1s2..sn-1sn creates n-2 words of length 3: w1 = s1s2s3, w2 = s2s3s4,
w3 = s3s4s5, wn-2 = sn-2sn-1sn
2) if word wi is not in graph, it will create
3) for every pair of words (wi, wi+1) add oriented edge of weight = 1, or increase the weight by 1
"""
from typing import Optional, Dict


class Vertex:
    def __init__(self, node):
        self._id = node
        self._adjacent = {}

    def __str__(self):
        return str(self.id)

    def add_neighbor(self, neighbor, weight=1) -> bool:
        if neighbor not in self._adjacent:
            self._adjacent[neighbor] = weight
            return True
        else:
            self._adjacent[neighbor] += 1
            return False

    def get_connections(self):
        return self._adjacent.keys()

    @property
    def id(self) -> int:
        return self._id

    @property
    def adjacent(self) -> {}:
        return self._adjacent

    def get_weight(self, neighbor) -> int:
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self._vert_dict = {}
        self._amount_of_edges = 0
        self._num_vertices = 0

    def __iter__(self):
        return iter(self._vert_dict.values())

    def add_vertex(self, node) -> Vertex:
        if node not in self._vert_dict:
            self._num_vertices = self._num_vertices + 1
            new_vertex = Vertex(node)
            self._vert_dict[node] = new_vertex
            return new_vertex
        else:
            return self._vert_dict[node]

    def get_vertex(self, n) -> Optional[Vertex]:
        if n in self._vert_dict:
            return self._vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=1) -> None:
        if frm not in self._vert_dict:
            self.add_vertex(frm)
        if to not in self._vert_dict:
            self.add_vertex(to)

        new_edge = self._vert_dict[frm].add_neighbor(self._vert_dict[to], cost)
        if new_edge:
            self._amount_of_edges += 1

        # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    @property
    def vert_dict(self) -> Dict[Vertex]:
        return self._vert_dict

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def amount_of_edges(self) -> int:
        return self._amount_of_edges


T = int(input())
g = Graph()
for _ in range(T):
    s = input()
    previous = None
    if len(s) > 0:
        word = s[0:3]
        g.add_vertex(word)
        previous = word

    for i in range(1, len(s) - 2):
        word = s[i:i + 3]
        g.add_vertex(word)
        g.add_edge(previous, word)
        previous = word


print(g.num_vertices)
print(g.amount_of_edges)
vert_dict = g.vert_dict
for vertex in vert_dict.values():
    adjacent = vertex.adjacent
    for key, value in adjacent.items():
        print(str(vertex.id) + " " + str(key) + " " + str(value))
