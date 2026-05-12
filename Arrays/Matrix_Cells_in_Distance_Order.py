"""
Problem Description:
    - You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the 
    cell with the coordinates (rCenter, cCenter).
    - Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the 
    smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.
    - The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

Constraints:
    - 1 <= rows, cols <= 100
    - 0 <= rCenter < rows
    - 0 <= cCenter < cols
"""

def allCellsDistOrder(rows, cols, rCenter, cCenter):
    """
    :type rows: int
    :type cols: int
    :type rCenter: int
    :type cCenter: int
    :rtype: List[List[int]]
    """
    distance = 0
    temp = []
    for r in range(rows):
        for c in range(cols):
            distance = abs(r - rCenter) + abs(c - cCenter)
            temp.append([distance, r, c])
    temp.sort(key = lambda x: x[0]) #sort based on distance from (rCenter, cCenter)

    result = []
    for dist, row, col in temp:
        result.append([row, col])
    
    return result

rows = 1
cols = 2
rCenter = 0
cCenter = 0
print(allCellsDistOrder(rows, cols, rCenter, cCenter))   #[[0, 0], [0, 1]]

rows2 = 2
cols2 = 2
rCenter2 = 0
cCenter2 = 1
print(allCellsDistOrder(rows2, cols2, rCenter2, cCenter2))   #[[0, 1], [0, 0], [1, 1], [1, 0]]

rows3 = 2
cols3 = 3
rCenter3 = 1
cCenter3 = 2
print(allCellsDistOrder(rows3, cols3, rCenter3, cCenter3))   #[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]