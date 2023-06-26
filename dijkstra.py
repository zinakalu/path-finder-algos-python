from graph_constructor import Graph

class DijkstraGraph(Graph):
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph} 
        distances[start] = 0 
        visited = set()

        while visited != set(self.graph): 
            u = min(distances, key=distances.get) 
            visited.add(u)

            for v, weight in self.graph[u].items():
                if v not in visited and distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight

        return distances 