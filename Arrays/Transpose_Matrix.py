# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 09:13:49 2025

@author: jwang
"""

def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    transposed = []
    for r in range(len(matrix[0])):
        sublist = []
        for c in range(len(matrix)):
            sublist.append(0)
        transposed.append(sublist)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            transposed[c][r] = matrix[r][c]
    
    return transposed

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Transposing", matrix, "results in", transpose(matrix))

matrix2 = [[1,2,3],[4,5,6]]
print("Transposing", matrix2, "results in", transpose(matrix2))

matrix3 = [[2,4,-1],[-10,5,11],[18,-7,6]]
print("Transposing", matrix3, "results in", transpose(matrix3))


