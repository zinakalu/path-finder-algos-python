from pathfinding.graph_constructor import Graph

class FloydWarshallGraph(Graph):
    def floyd_warshall(self):
        dist = self.graph
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist