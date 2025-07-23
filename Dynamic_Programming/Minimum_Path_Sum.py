# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 15:09:39 2025

@author: jwang

Problem Description:
    Given a m x n grid filled with non-negative numbers, find a path from top 
    left to bottom right, which minimizes the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
"""

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    for i in range(1, len(grid)):
        grid[i][0] += grid[i - 1][0]
    
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i - 1]
    
    for r in range(1, len(grid)):
        for c in range(1, len(grid[r])):
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
    
    return grid[len(grid) - 1][len(grid[0]) - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid)) #7 -> 1 + 3 + 1 + 1 + 1 = 7

grid2 = [[1,2,3],[4,5,6]]
print(minPathSum(grid2))    #12 -> 1 + 5 + 6 = 12
