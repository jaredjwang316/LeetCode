"""
Problem Description:
    - There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 
    (inclusive). The edges in the graph are represented as a 2D integer array edges, where each 
    edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair 
    is connected by at most one edge, and no vertex has an edge to itself.
    - You want to determine if there is a valid path that exists from vertex source to vertex destination.
    - Given edges and the integers n, source, and destination, return true if there is a valid path from 
    source to destination, or false otherwise.

Constraints:
    - 1 <= n <= 2 * 10^5
    - 0 <= edges.length <= 2 * 10^5
    - edges[i].length == 2
    - 0 <= ui, vi <= n - 1
    - ui != vi
    - 0 <= source, destination <= n - 1
    - There are no duplicate edges.
    - There are no self edges.
"""

def validPath(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    build_graph = dict()

    for i in range(n):
        build_graph[i] = []
    
    for edge in edges:
        #bi-directional graph
        build_graph[ edge[0] ].append(edge[1])
        build_graph[ edge[1] ].append(edge[0])
    
    visited = set()

    def dfs(node):
        if node == destination: #if there is a valid path to the destination
            return True
        
        visited.add(node)

        for neighbor in build_graph[node]:
            if neighbor not in visited:
                if dfs(neighbor) == True:
                    return True
    
        return False    #no way to reach the destination

    return dfs(source)

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(validPath(n, edges, source, destination)) #True

n2 = 6
edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source2 = 0
destination2 = 5
print(validPath(n2, edges2, source2, destination2)) #False

n3 = 10
edges3 = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source3 = 5
destination3 = 9
print(validPath(n3, edges3, source3, destination3)) #True