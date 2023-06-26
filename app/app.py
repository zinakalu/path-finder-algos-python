
from flask import Flask
from pathfinding.graph_constructor import Graph
from pathfinding.deepth_first_search import DFSGraph

app = Flask(__name__)


@app.route('/a_star')
def a_star():
    return 'Hello World'


@app.route('/dijkstra')
def dijkstra():
    pass

@app.route('/bellman_ford')
def bellman_ford():
    pass
@app.route('/breadth_first_search')
def breadth_first_search():
    pass



@app.route('/depth_first_search')
def deepth_first_search():
    # graph = Graph(4)
    # graph.add_edge(0,1,1)
    # graph.add_edge(1,2,3)
    # graph.add_edge(2,3, 2)
    
    # dfs = DFSGraph(graph)
    
    graph = DFSGraph(4, 0)
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,3)
    graph.add_edge(2,3, 2)
    print(graph.dfs_post_order())
    return graph.dfs_post_order()



@app.route('/floyd_warshall')
def floyd_warshall():
    pass










if __name__ == '__main__':
    app.run()