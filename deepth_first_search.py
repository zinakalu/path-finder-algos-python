from graph_constructor import Graph

class DFSGraph(Graph):
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
    
        traverse(self.root)
        return results


    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value) 

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