"""
Problem Description:
    - Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, 
    return true if these points are a boomerang.
    - A boomerang is a set of three points that are all distinct and not in a straight line.

Constraints:
    points.length == 3
    points[i].length == 2
    0 <= xi, yi <= 100
"""

def isBoomerang(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    points.sort(key = lambda x: x[0])   #sort the points based on x-coordinates
    if points[0] == points[1] or points[1] == points[2]:    #two points always form a straight line
        return False

    if points[0][0] == points[1][0]:    #special case: undefined slope
        if points[2][0] != points[1][0]:    #vertical line not formed
            return True
        else:
            return False

    if points[1][0] == points[2][0]:    #another special case for undefined slope
        if points[1][0] != points[0][0]:    #vertical line not formed
            return True
        else:
            return False
    
    slope1 = float(points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
    slope2 = float(points[2][1] - points[1][1]) / (points[2][0] - points[1][0])

    if slope1 != slope2:    #a straight line has the same slope
        return True
    return False

points = [[1,1],[2,3],[3,2]]
print(isBoomerang(points))  #True

points2 = [[1,1],[2,2],[3,3]]
print(isBoomerang(points2)) #False

points3 = [[0,0],[0,2],[2,1]]
print(isBoomerang(points3)) #True

points4 = [[0,0],[1,1],[1,1]]
print(isBoomerang(points4)) #False

points5 = [[0,0],[2,1],[2,2]]
print(isBoomerang(points5)) #True

points6 = [[52,86],[12,65],[24,71]]
print(isBoomerang(points6)) #True