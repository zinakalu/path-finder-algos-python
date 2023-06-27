from .graph_constructor import Graph

class DijkstraGraph(Graph):
    def dijkstra(self, start, max_depth=100):
        distances = {node: float('inf') for node in self.graph} 
        distances[start] = 0 
        visited = set()
        depth = 0

        while visited != set(self.graph) and depth < max_depth: 
            u = min(distances, key=distances.get) 
            visited.add(u)

            for v, weight in self.graph[u].items():
                if v not in visited and distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight

            depth += 1
        return distances 