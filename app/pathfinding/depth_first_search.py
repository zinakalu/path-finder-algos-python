from .graph_constructor import Graph #or pathfinding.graph_constructor


class DFSGraph(Graph):
    def __init__(self, vertices, root):
        super().__init__(vertices)
        self.root = root
        self.visited = set()


    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if not neighbor in self.visited:
                    self.visited.add(neighbor)
                    traverse(neighbor)
            results.append(current_node)

        traverse(self.root)
        return results 

    def dfs_pre_order(self):
        results = []

        def traverse(current_node): 
            results.append(current_node)
            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    traverse(neighbor)

        traverse(self.root) 
        return results