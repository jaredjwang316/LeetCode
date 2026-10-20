"""
Problem Description:
    - There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly 
    n - 1 edges that connect the center node with every other node.
    - You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the 
    center of the given star graph.

Constraints:
    - 3 <= n <= 10^5
    - edges.length == n - 1
    - edges[i].length == 2
    - 1 <= ui, vi <= n
    - ui != vi
    - The given edges represent a valid star graph.
"""

def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """
    graph = dict()
    for i in range(1, len(edges) + 2, 1):
        graph[i] = []
    
    for edge in edges:
        source = edge[0]
        destination = edge[1]

        graph[source].append(destination)
        graph[destination].append(source)
    
    for k,v in graph.items():
        if len(v) == len(graph) - 1:
            return k
    
    return -1

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))    #Output: 2

edges2 = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges2))   #Output: 1