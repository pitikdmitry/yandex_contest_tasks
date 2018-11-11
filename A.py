class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=1):
        if neighbor not in self.adjacent:
            self.adjacent[neighbor] = weight
        else:
            self.adjacent[neighbor] += 1

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        if node not in self.vert_dict:
            self.num_vertices = self.num_vertices + 1
            new_vertex = Vertex(node)
            self.vert_dict[node] = new_vertex
            return new_vertex
        else:
            return self.vert_dict[node]

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=1):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def vertices_amount(self):
        return self.num_vertices



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


print(g.vertices_amount())
