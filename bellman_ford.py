from graph_constructor import Graph

class BellmanGraph(Graph):
    def bellman_ford(self, src):
        distance = [float('inf')]* self.vertices
        distance[src] = 0

        for _ in range(self.vertices -1): 
            for edge in self.graph:     
                if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
                distance[edge.v] = distance[edge.u] + edge.weight

        for edge in self.graph:     
            if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
                print("Graph contains negative weight cycle")
                return

        return distance