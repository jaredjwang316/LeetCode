"""
Problem Description:
    - A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or 
    leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the 
    matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], 
    and mat[4][2].
    - Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the 
    resulting matrix.

Constraints:
    - m == mat.length
    - n == mat[i].length
    - 1 <= m, n <= 100
    - 1 <= mat[i][j] <= 100
"""

def diagonalSort(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    for start_row in range(len(mat)):   #go over all diagonals that start on leftmost column
        curr_row = start_row
        curr_col = 0

        values = []

        while(curr_row < len(mat) and curr_col < len(mat[0])):
            values.append(mat[curr_row][curr_col])

            curr_row += 1
            curr_col += 1

        values.sort()

        curr_row = start_row
        curr_col = 0

        count = 0   #keep track of the index that we are currently at in the values list
        while(curr_row < len(mat) and curr_col < len(mat[0])):
            mat[curr_row][curr_col] = values[count]

            curr_row += 1
            curr_col += 1
            count += 1
    
    for start_col in range(len(mat[0])):    #go over all diagonals that start on topmost row
        curr_row = 0
        curr_col = start_col

        values = []

        while(curr_row < len(mat) and curr_col < len(mat[0])):
            values.append(mat[curr_row][curr_col])

            curr_row += 1
            curr_col += 1
        
        values.sort()

        curr_row = 0
        curr_col = start_col

        count = 0   #keep track of the index that we are currently at in the values list
        while(curr_row < len(mat) and curr_col < len(mat[0])):
            mat[curr_row][curr_col] = values[count]

            curr_row += 1
            curr_col += 1
            count += 1

    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(diagonalSort(mat))    #Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

mat2 = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
print(diagonalSort(mat2))   #Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]