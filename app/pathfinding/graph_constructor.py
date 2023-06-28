class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph = [[0 for _ in range(vertices)] for __ in range(vertices)]
        self.graph = {v: {} for v in range(vertices) }

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def neighbors(self, v):
        return self.graph[v].keys()