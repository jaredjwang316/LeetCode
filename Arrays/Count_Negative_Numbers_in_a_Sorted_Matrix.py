"""
Problem Description:
    - Given a m x n matrix grid which is sorted in non-increasing order both row-wise 
    and column-wise, return the number of negative numbers in grid.

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 100
    - -100 <= grid[i][j] <= 100
"""

def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count_negatives = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] < 0:
                count_negatives = count_negatives + (len(grid[r]) - c)
                break   #rest of the cells in this row are all negative numbers
    
    return count_negatives

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print("Number of negative numbers in the grid is", countNegatives(grid))    #8

grid2 = [[3,2],[1,0]]
print("Number of negative numbers in the grid is", countNegatives(grid2))   #0

grid3 = [[5,1,0],[-5,-5,-5]]
print("Number of negative numbers in the grid is", countNegatives(grid3))   #3