
from flask import Flask
from pathfinding.graph_constructor import Graph
from pathfinding.depth_first_search import DFSGraph
from pathfinding.dijkstra import DijkstraGraph
# import ipdb

app = Flask(__name__)


@app.route('/a_star')
def a_star():
    return 'Hello World'


@app.route('/dijkstra')
def dijkstra():
    graph = DijkstraGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 6)

    max_iterations = 100
    distances = graph.dijkstra(start=0, max_iterations=max_iterations)

    return str(distances)

@app.route('/bellman_ford')
def bellman_ford():
    pass
@app.route('/breadth_first_search')
def breadth_first_search():
    pass



def depth_first_search(graph, traversal_type):
    if traversal_type == "post_order":
        return DFSGraph(graph, root=0).dfs_post_order()
    elif traversal_type == "pre_order":
        return DFSGraph(graph, root=0).dfs_pre_order()
    else: 
        raise ValueError("Invalid traversal type")
    

@app.route('/depth_first_search/<traversal_type>')
def dfs(traversal_type):
    graph = DFSGraph(vertices=4, root=0)
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,3)
    graph.add_edge(2,3, 2)

    return depth_first_search(graph, traversal_type)


@app.route('/floyd_warshall')
def floyd_warshall():
    pass










if __name__ == '__main__':
    app.run()