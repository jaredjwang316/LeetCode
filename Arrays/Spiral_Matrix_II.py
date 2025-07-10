# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 12:33:32 2025

@author: jwang

Problem Description:
    Given a positive integer n, generate an n x n matrix filled with elements 
    from 1 to n^2 in spiral order.

Constraints:
    1 <= n <= 20
"""

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    
    result = []

    for i in range(n):
        sub_list = []
        for j in range(n):
            sub_list.append(0)
        result.append(sub_list)
    
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    count = 1
    while(top <= bottom and left <= right):
        if (count > n * n):
            break
        
        for i in range(left, right + 1, 1):
            result[top][i] = count
            count += 1
        top += 1

        if (count > n * n):
            break

        for i in range(top, bottom + 1, 1):
            result[i][right] = count
            count += 1
        right -= 1

        if (count > n * n):
            break

        for i in range(right, left - 1, -1):
            result[bottom][i] = count
            count += 1
        bottom -= 1

        if (count > n * n):
            break

        for i in range(bottom, top - 1, -1):
            result[i][left] = count
            count += 1
        left += 1
    
    return result

n = 3
print(generateMatrix(n))

n2 = 1
print(generateMatrix(n2))
