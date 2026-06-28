"""
Problem Description:
    - You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
        * Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
        * Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
    - Return true if all the cells satisfy these conditions, otherwise, return false.

Constraints:
    - 1 <= n, m <= 10
    - 0 <= grid[i][j] <= 9
"""

def satisfiesConditions(grid):
    """
    :type grid: List[List[int]]
    :rtype: bool
    """
    for r in range(len(grid)):
        for c in range(1, len(grid[0])):
            if grid[r][c] == grid[r][c - 1]:    #if neighboring left cell equals current cell
                return False
    
    for r in range(len(grid) - 1):
        for c in range(len(grid[0])):
            if grid[r][c] != grid[r + 1][c]:    #if the cell below the current cell is not equal
                return False
    
    return True

grid = [[1,0,2],[1,0,2]]
print(satisfiesConditions(grid))    #true

grid2 = [[1,1,1],[0,0,0]]
print(satisfiesConditions(grid2))   #false

grid3 = [[1],[2],[3]]
print(satisfiesConditions(grid3))   #false

grid4 = [[4,4],[4,4]]
print(satisfiesConditions(grid4))   #false
