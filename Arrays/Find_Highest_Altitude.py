# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 23:18:11 2025

@author: jwang

Problem Description:
    There is a biker going on a road trip. The road trip consists of n + 1 points 
    at different altitudes. The biker starts his trip on point 0 with altitude 
    equal 0.
    You are given an integer array gain of length n where gain[i] is the net gain 
    in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the 
    highest altitude of a point.

Constraints:
    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100
"""

def largestAltitude(gain):
    """
    :type gain: List[int]
    :rtype: int
    """
    altitudes = [0, gain[0]]
    for i in range(1, len(gain)):
        altitudes.append(altitudes[i] + gain[i])
    return max(altitudes)

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))    #1

gain2 = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain2))   #0