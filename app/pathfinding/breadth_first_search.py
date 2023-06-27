from collections import deque
from pathfinding.graph_constructor import Graph

class BFSGraph(Graph):
     def breadth_first_search(self, start):
        self.visited = set()
        queue = deque([start])
        results=[]


        while queue:
            current_node = queue.popleft()
            results.append(current_node.value)
            self.visited.add(current_node.value)

            for neighbor in self.graph[current_node]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                
        return results