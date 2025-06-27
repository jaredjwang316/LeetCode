# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 10:22:01 2025

@author: jwang

Problem Description:
    Given the coordinates of four points in 2D space p1, p2, p3 and p4, return 
    true if the four points construct a square.
    The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    
Important Constraints:
    p1.length == p2.length == p3.length == p4.length == 2
    -10^4 <= xi, yi <= 10^4
"""

import math

def dist_formula(x1, y1, x2, y2):
    x_dist = abs(x1 - x2)
    y_dist = abs(y1 - y2)
    return math.sqrt(pow(x_dist, 2) + pow(y_dist, 2))

def validSquare(p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    points = [p1, p2, p3, p4]
    distances = []
    for p in range(len(points) - 1):
        for q in range(p + 1, len(points)):
            distances.append(dist_formula( (points[p])[0], (points[p])[1], (points[q])[0], (points[q])[1]) )
    distances.sort()
    check1 = (distances[0] == distances[1] == distances[2] == distances[3])
    if check1 == False:
        return False
    
    check2 = (distances[4] == distances[5])
    if check2 == False:
        return False

    check3 = (distances[3] == distances[4])
    if check3 == True:
        return False

    return True

p1 = [0,0]
p2 = [1,1] 
p3 = [1,0] 
p4 = [0,1]
print(validSquare(p1, p2, p3, p4))

p5 = [0,0] 
p6 = [1,1] 
p7 = [1,0] 
p8 = [0,12]
print(validSquare(p5, p6, p7, p8))

p9 = [1,0] 
p10 = [-1,0] 
p11 = [0,1] 
p12 = [0,-1]
print(validSquare(p9, p10, p11, p12))

p13 = [0,0] 
p14 = [0,0] 
p15 = [0,0] 
p16 = [0,0]
print(validSquare(p13, p14, p15, p16))