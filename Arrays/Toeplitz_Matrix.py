# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 14:28:22 2025

@author: jwang

Problem Description:
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
"""

def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r < len(matrix) - 1 and c < len(matrix[r]) - 1:
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
    
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(matrix, "is Toeplitz?", isToeplitzMatrix(matrix))

matrix2 = [[1,2],[2,2]]
print(matrix2, "is Toeplitz?", isToeplitzMatrix(matrix2))