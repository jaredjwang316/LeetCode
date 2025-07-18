# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:09:53 2025

@author: jwang

Problem Description:
    Given an m x n integer matrix matrix, if an element is 0, set its entire 
    row and column to 0's.
    Note: You must do it in place.

Constraints:
    
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1
"""

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    row_to_set_zeros = []
    col_to_set_zeros = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                row_to_set_zeros.append(r)
                col_to_set_zeros.append(c)
    
    for r in row_to_set_zeros:
        for c in range(len(matrix[r])):
            matrix[r][c] = 0
    
    for c in col_to_set_zeros:
        for r in range(len(matrix)):
            matrix[r][c] = 0
            
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print("Original matrix:", matrix)
setZeroes(matrix)
print("After calling setZeros(), matrix:", matrix)  #[[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("Original matrix:", matrix2)
setZeroes(matrix2)
print("After calling setZeros(), matrix:", matrix2) #[[0,0,0,0],[0,4,5,0],[0,3,1,0]]