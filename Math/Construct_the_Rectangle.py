# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 15:26:32 2025

@author: jwang
"""

"""
Problem Description:
    A web developer needs to know how to design a web page's size. 
    So, given a specific rectangular web page’s area, your job by now is to 
    design a rectangular web page, whose length L and width W satisfy the 
    following requirements:

        - The area of the rectangular web page you designed must 
          equal to the given target area.
        - The width W should not be larger than the length L
        - The difference between length L and width W should be as small as possible.

    Return an array [L, W] where L and W are the length and width of the rectangle.

Important Constraint:
    area is a positive integer that is greater than or equal to 1
"""

import math

def constructRectangle(area):
    """
    :type area: int
    :rtype: List[int]
    """
    length = 0
    width = 0
    for i in range(2, int(math.sqrt(area) + 1) ):
        if area % i == 0:
            #make sure length is already greater than or equal to width
            if i > area // i:
                length = i, 
                width = area // i
            else:
                length = area // i
                width = i
    
    if length != 0 and width != 0:  #in this case, area is composite number
        return [length, width]

    return [area, 1]    #if the area is a prime number or 1


print(constructRectangle(4))    #should return [2, 2] as it is more optimal than [4, 1]
print(constructRectangle(37))   #should return be [37, 1] since 37 is prime
print(constructRectangle(1))    #should be [1, 1] since 1 is the only integer that divides 1
print(constructRectangle(122122))   #should return [427,286] 
print(constructRectangle(289))  #should return [17, 17] since 17^2 = 289 and 17 is prime
print(constructRectangle(247))  #should return [19, 13] since 247 = 13 * 19 

