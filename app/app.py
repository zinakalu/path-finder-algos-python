
from flask import Flask, jsonify
import requests
from pathfinding.graph_constructor import Graph
from pathfinding.depth_first_search import DFSGraph
from pathfinding.dijkstra import DijkstraGraph
from pathfinding.floyd_warshall import FloydWarshallGraph
from pathfinding.breadth_first_search import BFSGraph
from pathfinding.bellman_ford import BellmanGraph
from pathfinding.a_star import AStarGraph
# import ipdb

app = Flask(__name__)


@app.route('/a_star')
def a_star():
    graph = AStarGraph(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 1)

    return graph.a_star(0, 3)

@app.route('/dijkstra')
def dijkstra():
    graph = DijkstraGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 6)

    start = 0
    distances = graph.dijkstra(start)
    
    

    return jsonify(distances)

@app.route('/bellman_ford')
def bellman_ford():
    graph = BellmanGraph(10)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)
    graph.add_edge(4, 5, 8)
    graph.add_edge(5, 6, 9)
    graph.add_edge(6, 7, 10)

    return jsonify(graph.bellman_ford(0))



@app.route('/breadth_first_search')
def breadth_first_search():
    graph = BFSGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 1)
    graph.add_edge(0, 3, 5)

    return graph.breadth_first_search(0)


@app.route('/depth_first_search')
def dfs():
    graph = DFSGraph(vertices=4)
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,3)
    graph.add_edge(2,3, 2)

    return graph.dfs(0)


@app.route('/floyd_warshall')
def floyd_warshall():
    graph = FloydWarshallGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 1)
    graph.add_edge(0, 3, 5)

    return graph.floyd_warshall()









if __name__ == '__main__':
    app.run()