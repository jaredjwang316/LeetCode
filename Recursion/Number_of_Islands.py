# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 20:00:10 2025

@author: jwang

Problem Description:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) 
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are 
    all surrounded by water.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""

def dfs(grid, row, col):
    #check if we are our of boundary
    if row < 0 or row >= len(grid):
        return
    if col < 0 or col >= len(grid[row]):
        return

    if grid[row][col] == '1':
        grid[row][col] = '0'    #mark as visited
        dfs(grid, row - 1, col) #up
        dfs(grid, row + 1, col) #down
        dfs(grid, row, col - 1) #left
        dfs(grid, row, col + 1) #right
                

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':   #if we encounter land
                dfs(grid, r, c)
                count_islands += 1
    
    return count_islands
    
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print("The number of islands in", grid, "is", numIslands(grid))

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("The number of islands in", grid2, "is", numIslands(grid2))


