# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:14:47 2025

@author: jwang
"""
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2 and n >= 1: 
        return n
        
    first = 1
    second = 2
    result = 0
    for i in range(2, n):
        result = first + second
        first = second
        second = result

    return result


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(6))
print(climbStairs(45))