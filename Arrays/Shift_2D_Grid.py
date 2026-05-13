"""
Problem Description:
    - Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
    - In one shift operation:
        *Element at grid[i][j] moves to grid[i][j + 1].
        *Element at grid[i][n - 1] moves to grid[i + 1][0].
        *Element at grid[m - 1][n - 1] moves to grid[0][0].
    - Return the 2D grid after applying shift operation k times.

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m <= 50
    - 1 <= n <= 50
    - -1000 <= grid[i][j] <= 1000
    - 0 <= k <= 100
"""

def shiftGrid(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    if k == 0:  #edge case: no shifting needed
        return grid

    newGrid = []
    for r in range(len(grid)):
        subList = []
        for c in range(len(grid[r])):
            subList.append(0)
        newGrid.append(subList)
    
    for i in range(k):
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                #elements at the last column goes to the first columm
                newGrid[r][(c + 1) % len(grid[r])] = grid[r][c] 

        temp = newGrid[-1][0]
        for r in range(1, len(newGrid)):
            newGrid[r][0] = grid[r - 1][-1] # Elements at grid[i][n - 1] moves to grid[i + 1][0]
        newGrid[0][0] = temp    # Element at grid[m - 1][n - 1] moves to grid[0][0].

        for r in range(len(newGrid)):
            for c in range(len(newGrid[r])):
                grid[r][c] = newGrid[r][c]
    return newGrid

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(shiftGrid(grid, k)) # [[9,1,2],[3,4,5],[6,7,8]]

grid2 = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k2 = 4
print(shiftGrid(grid2, k2)) # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

grid3 = [[1,2,3],[4,5,6],[7,8,9]]
k3 = 9
print(shiftGrid(grid3, k3)) # [[1,2,3],[4,5,6],[7,8,9]]

grid4 = [[100]]
k4 = 0
print(shiftGrid(grid4, k4)) # [[100]]