"""
Problem Description:
    - An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
    - Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 100
    - 1 <= matrix[i][j] <= n
"""

def checkValid(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    
    row_set = set()

    for r in range(len(matrix)):    #row-based traversal, checking whether each row contains all the integers from 1 to n inclusive
        row_set = set()
        for c in range(len(matrix[0])):
            row_set.add(matrix[r][c])
        
        if len(row_set) != len(matrix):
            return False
    
    col_set = set()
    for c in range(len(matrix[0])): #column-based traversal, checking whether each column contains all the integers from 1 to n inclusive
        col_set = set()
        for r in range(len(matrix)):
            col_set.add(matrix[r][c])
        
        if len(col_set) != len(matrix[0]):
            return False
    
    return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(checkValid(matrix))   #True

matrix2 = [[1,1,1],[1,2,3],[1,2,3]]
print(checkValid(matrix2))  #False