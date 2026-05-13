"""
Problem Description:
    - There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are 
    represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal 
    diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

    - Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
    A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the 
    number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

    - Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Constraints:
    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= xstart < xend <= 2^31 - 1
"""

def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key = lambda x: x[1])   #sort the points based on their endpoint value

    end = points[0][1]
    num_arrows = 1
    for i in range(1, len(points)):
        if points[i][0] > end:
            num_arrows += 1
            end = points[i][1]
    
    return num_arrows

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))   # 2

points2 = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points2))   # 4

points3 = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points3))   # 2