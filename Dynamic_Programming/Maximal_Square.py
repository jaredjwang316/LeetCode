# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 14:11:18 2025

@author: jwang

Problem Description:
    Given an m x n binary matrix filled with 0's and 1's, find the largest 
    square containing only 1's and return its area.
    
Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""

def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    dp = []
    for r in range(len(matrix)):
        subList = []
        for c in range(len(matrix[r])):
            if matrix[r][c] == '0':
                subList.append(0)
            else:
                subList.append(1)
        dp.append(subList)

    maxSide = 0
    for r in range(len(dp)):
        if matrix[r][0] == '1':
            maxSide = 1
    
    for c in range(len(dp[0])):
        if matrix[0][c] == '1':
            maxSide = 1
    
    for r in range(1, len(dp)):
        for c in range(1, len(dp[r])):
            if matrix[r][c] == '1':
                dp[r][c] += min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1])
                maxSide = max(maxSide, dp[r][c])

    return maxSide * maxSide

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))    #4

matrix2 = [["0","1"],["1","0"]]
print(maximalSquare(matrix2))   #1

matrix3 = [["0"]]
print(maximalSquare(matrix3))   #0