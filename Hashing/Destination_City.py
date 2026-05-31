"""
Problem Description:
    - You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct 
    path going from cityAi to cityBi. Return the destination city, that is, the city without any path 
    outgoing to another city.
    - It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be 
    exactly one destination city.

Constraints:
    - 1 <= paths.length <= 100
    - paths[i].length == 2
    - 1 <= cityAi.length, cityBi.length <= 10
    - cityAi != cityBi
    - All strings consist of lowercase and uppercase English letters and the space character.
"""

def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    direct_paths = dict()
    for path in paths:
        direct_paths[ path[0] ] = path[1]
    
    for val in direct_paths.values():
        if val not in direct_paths.keys():
            return val
    return ""

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))   # Output: "Sao Paulo"

path2 = [["B","C"],["D","B"],["C","A"]]
print(destCity(path2))   # Output: "A"

path3 = [["A","Z"]]
print(destCity(path3))   # Output: "Z"