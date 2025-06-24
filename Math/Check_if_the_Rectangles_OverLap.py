# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 08:55:10 2025

@author: jwang

Problem Description:
    An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], 
    where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) 
    is the coordinate of its top-right corner. Its top and bottom edges are 
    parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

    Two rectangles overlap if the area of their intersection is positive. To be 
    clear, two rectangles that only touch at the corner or edges do not overlap.

    Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, 
    otherwise return false.

Constraints:
    
    rec1.length == 4
    rec2.length == 4
    -10^9 <= rec1[i], rec2[i] <= 10^9
    rec1 and rec2 represent a valid rectangle with a non-zero area.

"""

def isRectangleOverlap(rec1, rec2):
    """
    :type rec1: List[int]
    :type rec2: List[int]
    :rtype: bool
    """
    #compare the position of the x-coordinate of top-right corner of a rectangle and bottom-right corner of the other
    if rec1[2] <= rec2[0] or rec1[0] >= rec2[2]:
        return False
    
    if rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
        return False
    
    return True

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(isRectangleOverlap(rec1, rec2))   #True

rec3 = [0,0,1,1]
rec4 = [1,0,2,1]
print(isRectangleOverlap(rec3, rec4))   #False

rec5 = [0,0,1,1]
rec6 = [2,2,3,3]
print(isRectangleOverlap(rec5, rec6))   #False

rec7 = [5,15,8,18]
rec8 = [0,3,7,9]
print(isRectangleOverlap(rec7, rec8))   #False