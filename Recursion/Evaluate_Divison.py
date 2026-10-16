"""
Problem Description:
    - You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the 
    equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
    - You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
    - Return the answers to all queries. If a single answer cannot be determined, return -1.0.

    - Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
    - Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Constraints:
    - 1 <= equations.length <= 20
    - equations[i].length == 2
    - 1 <= Ai.length, Bi.length <= 5
    - values.length == equations.length
    - 0.0 < values[i] <= 20.0
    - 1 <= queries.length <= 20
    - queries[i].length == 2
    - 1 <= Cj.length, Dj.length <= 5
    - Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    graph = {}

    for i in range(len(equations)):
        u = equations[i][0]
        v = equations[i][1]
        value = values[i]

        if u not in graph:
            graph[u] = {}
        
        if v not in graph:
            graph[v] = {}
        
        graph[u][v] = value # Say equations[i] = [A, B], then A / B = value
        graph[v][u] = 1 / value # B / A = 1 / (A / B) = 1 / value, the reciprocal of value
    
    def dfs(source, destination, visited):
        if source == destination:   #dividing a number by itself always results in 1.0
            return 1.0
        
        visited.add(source)

        for nextSource, weight in graph[source].items():
            if nextSource not in visited:   #avoid redundant traversal
                temp = dfs(nextSource, destination, visited)
                if temp != -1.0:    # if this path was not a dead end (valid path to destination found)
                    return weight * temp
        
        return -1.0
    
    result = []

    for query in queries:
        s = query[0]
        d = query[1]
        
        # The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
        if s not in graph or d not in graph:
            result.append(-1.0)
        else:
            result.append( dfs(s, d, set()) )
    
    return result

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries)) #Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations2 = [["a","b"],["b","c"],["bc","cd"]]
values2 = [1.5,2.5,5.0]
queries2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(calcEquation(equations2, values2, queries2))  #Output: [3.75000,0.40000,5.00000,0.20000]

equations3 = [["a","b"]]
values3 = [0.5]
queries3 = [["a","b"],["b","a"],["a","c"],["x","y"]]
print(calcEquation(equations3, values3, queries3))  #Output: [0.50000,2.00000,-1.00000,-1.00000]

equations4 = [["a","b"],["a","c"],["d","e"],["d","f"],["a","d"],["aa","bb"],["aa","cc"],["dd","ee"],["dd","ff"],["aa","dd"],["a","aa"]]
values4 = [2.0,3.0,4.0,5.0,7.0,5.0,8.0,9.0,3.0,2.0,2.0]
queries4 = [["ff","a"]]
print(calcEquation(equations4, values4, queries4))  #Output: [0.08333]