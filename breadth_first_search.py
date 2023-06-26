from collections import deque
from graph_constructor import Graph

class BFSGraph(Graph):
     def breadth_first_search(self):
        current_node = self.root
        queue = deque()
        results=[] 

        queue.append(current_node) 

        while queue: 
            current_node = queue.popleft()
            results.append(current_node.value) 

            if current_node.left is not None: 
                queue.append(current_node.left) 

            if current_node.right is not None: 
                queue.append(current_node.right) 
                
        return results