from graph_constructor import Graph

class AStarGraph(Graph):
    def a_start(self, start, goal):
        distances = {vertex: float("inf") for vertex in graph}
        distances[start] = 0
        open_list = []
        came_from = {}
        current_cost = {start: 0}

        heapq.heappush(open_list, (0, start))

        while open_list:
            current, priority = heapq.heappop(open_list) 

            if current == goal: 
                path = [] 
                while current != start: 
                    path.append(current) 
                    current = came_from[current] 
                path.reverse()
                return path 

            for neighbor, weight in graph[current].items(): 
                new_cost = current_cost[current] + weight 

                if neighbor not in current_cost or new_cost < current_cost[neighbor]:
                    current_cost[neighbor] = new_cost 
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (priority, neighbor))
                    came_from[neighbor] = current

        return None 


    def heuristic(self, node, goal):
        (x1, y1) = node
        (x2, y2) = goal
        return abs(x1 - x2) + abs(y1 - y2)