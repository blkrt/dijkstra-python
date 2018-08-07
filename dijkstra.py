__author__ = 'blkrt'

import networkx as nx
import matplotlib.pyplot as plt

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def dijkstra(graph, source, target):
    queue = []
    visited = {}
    distance = {}
    shortest_distance = {}
    parent = {}

    for node in range(len(graph)):
        distance[node] = None
        visited[node] = False
        parent[node] = None
        shortest_distance[node] = float("inf")

    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        current = queue.pop(0)
        visited[current] = True
        if current == target:
            print(backtrace(parent, source, target))
            #break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = distance[neighbor]
                    parent[neighbor] = current
                    queue.append(neighbor)
    print(distance)
    print(shortest_distance)
    print(parent)
    print(target)

def main():

    G=nx.Graph()
    G.add_weighted_edges_from([(0,1,0),(1,2,0)])

    dijkstra(G,0,2)
    nx.draw(G)

    plt.show()


if __name__ == "__main__":
    main()