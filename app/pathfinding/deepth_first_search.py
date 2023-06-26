from .graph_constructor import Graph

class DFSGraph(Graph):
    def __init__(self, vertices, root):
        super().__init__(vertices)
        self.root = root
        self.visited = set()

    # def dfs_in_order(self):
    #     results = []

    #     def traverse(current_node):
    #         neighbors = self.grapgh[current_node]

    #         for neighbor in neighbors:
    #             traverse(neighbor)

    #             traverse(current_node.right)
    
    #     traverse(self.root)
    #     return results


    def dfs_post_order(self):
        results = []

    
        def traverse(current_node):
            neighbors = self.graph[current_node]

            for neighbor in neighbors:
                if not neighbor in self.visited:
                    self.visited.add(neighbor)
                    results.append(neighbor)
                    traverse(neighbor)

        traverse(self.root)
        return results 


    def dfs_pre_order(self):
        results = []
        def traverse(current_node): 
            results.append(current_node.value) 
            if current_node.left is not None:  
                traverse(current_node.left) 
            if current_node.right is not None:
                traverse(current_node.right) 

        traverse(self.root) 
        return results