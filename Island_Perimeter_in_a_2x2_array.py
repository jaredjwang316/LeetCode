# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 20:06:36 2025

@author: jwang
"""

def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    island_perimeter = 0

    #row-based traversal
    for i in range(len(grid)):  
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                island_perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:   #if not in first row and the neighbor-top cell is island
                    island_perimeter -= 1    
                if j > 0 and grid[i][j - 1] == 1:   #if not in the first column and neighboring-left cell is island
                    island_perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:   #if not in bottom most row and bottom neighbor is island
                    island_perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:    #if not on right-most column and right neighbor is island
                    island_perimeter -= 1
    return island_perimeter 

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))

grid2 = [[1]]
print(islandPerimeter(grid2))

grid3 = [[1, 0]]
print(islandPerimeter(grid3))
