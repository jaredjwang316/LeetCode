"""
Problem Description:
    - You are given two integers, x and y, which represent your current location on a Cartesian 
    grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents 
    that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same 
    y-coordinate as your location.

    - Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your 
    current location. If there are multiple, return the valid point with the smallest index. If there 
    are no valid points, return -1.  The Manhattan distance between two points (x1, y1) and (x2, y2) 
    is abs(x1 - x2) + abs(y1 - y2).

Constraints:
    - 1 <= points.length <= 10^4
    - points[i].length == 2
    - 1 <= x, y, ai, bi <= 10^4
"""

def nearestValidPoint(x, y, points):
    """
    :type x: int
    :type y: int
    :type points: List[List[int]]
    :rtype: int
    """
    smallest_manhattan_dist = float('inf')
    for point in points:
        if point[0] == x or point[1] == y:
            smallest_manhattan_dist = min(smallest_manhattan_dist, abs(point[0] - x) + abs(point[1] - y))

    for i, point in enumerate(points):
        if (point[0] == x or point[1] == y) and abs(point[0] - x) + abs(point[1] - y) == smallest_manhattan_dist:
            return i    #return the valid with the smallest manhattan distance from your current location.  if there are multiple, return the one with smallest index.
    
    return -1

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(nearestValidPoint(x, y, points))  # Output: 2

x2 = 3
y2 = 4
points2 = [[3,4]]
print(nearestValidPoint(x2, y2, points2))  # Output: 0

x3 = 3
y3 = 4
points3 = [[2,3]]
print(nearestValidPoint(x3, y3, points3))  # Output: -1

x4 = 1
y4 = 1
points4 = [[1,2],[3,3],[3,3]]
print(nearestValidPoint(x4, y4, points4))  # Output: 0

