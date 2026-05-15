"""
Problem Description:
    - You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the 
    coordinate of a point. Check if these points make a straight line in the XY plane.

Constraints:
    - 2 <= coordinates.length <= 1000
    - coordinates[i].length == 2
    - -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    - coordinates contains no duplicate point.
"""

def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    count_vertical = 0
    for i in range(1, len(coordinates)):    #edge case: check whether a vertical line can be formed by given coordinates.  need to consider undefined slope case
        if coordinates[i][0] == coordinates[i - 1][0]:
            count_vertical += 1
    
    if count_vertical == len(coordinates) - 1:  #if all the coordinate points connect together end up forming a vertical line
        return True

    if coordinates[1][0] == coordinates[0][0]:  #if we get to here, we know that not all the given coordinates have the same x-coordinate
        return False
    
    slope = float(coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])

    for i in range(2, len(coordinates)):
        if coordinates[i][0] == coordinates[i - 1][0]:
            return False
        if float(coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0]) != slope:
            return False
    
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))    #True

coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates2))    #False

coordinates3 = [[0,0],[0,1],[0,-1]]
print(checkStraightLine(coordinates3))    #True

coordinates4 = [[1,1],[2,2],[2,0]]
print(checkStraightLine(coordinates4))    #False

coordinates5 = [[0,0],[0,5],[5,5],[5,0]]
print(checkStraightLine(coordinates5))    #False