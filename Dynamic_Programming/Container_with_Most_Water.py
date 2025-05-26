# -*- coding: utf-8 -*-
"""
Created on Mon May 26 17:06:55 2025

@author: jwang
"""

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxArea = 0
    left = 0
    right = len(height) - 1

    while(left <= right):
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left) )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

height1 = [1, 1]
print(maxArea(height1))