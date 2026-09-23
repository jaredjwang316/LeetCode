"""
Problem Description:
    - Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Constraints:
    - m == mat.length
    - n == mat[i].length
    - 1 <= m, n <= 10^4
    - 1 <= m * n <= 10^4
    - -10^5 <= mat[i][j] <= 10^5
"""

def findDiagonalOrder(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    #Define direction = 1 as up-right
    #Define direction = -1 as down-left
    direction = 1

    row = 0
    col = 0

    result = []
    while(row < len(mat) and col < len(mat[0])):
        result.append(mat[row][col])

        if direction == 1:
            if row == 0 and col == len(mat[0]) - 1:  #if we are currently at the top-right corner
                row += 1    #move down a row
                direction = -1
            elif row == 0:   #if we are currently at the topmost row but not at the top-right corner
                col += 1    #move to the neighboring right column
                direction = -1
            elif col == len(mat[0]) - 1:   #if we are currently at the rightmost column
                row += 1    #move down a row
                direction = -1
            else:   #continue moving in the up-right direction
                row -= 1
                col += 1
        else:
            if row == len(mat) - 1 and col == 0:    #if we are at the bottom-left corner
                col += 1    #move to the neighboring right column
                direction = 1 
            elif col == 0:    #if we are currently at the leftmost column but not the bottom-left corner
                row += 1    #move down a row
                direction = 1
            elif row == len(mat) - 1:   #if we are currently at the bottom-most row
                col += 1    #move to the neighboring right column
                direction = 1
            else:   #continue moving in the down-left direction
                row += 1
                col -= 1
    
    return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))   #Output: [1,2,4,7,5,3,6,8,9]

mat2 = [[1,2],[3,4]]
print(findDiagonalOrder(mat2))  #Output: [1,2,3,4]

mat3 = [[3],[2]]
print(findDiagonalOrder(mat3))  #Output: [3,2]

mat4 = [[2,5],[8,4],[0,-1]]
print(findDiagonalOrder(mat4))  #Output: [2,5,8,0,4,-1]