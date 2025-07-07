# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:26:51 2025

@author: jwang

Problem Description:
    Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    spiral_result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    #terminate when bounadries cross over
    while (top <= bottom and left <= right):
        #each iteration performa a clockwise iteration on the outermost non-visited boundary of the matrix

        if len(matrix) * len(matrix[0]) == len(spiral_result):
            break

        for i in range(left, right + 1):    #left to right
            spiral_result.append(matrix[top][i])
        top += 1
        
        if len(matrix) * len(matrix[0]) == len(spiral_result):
            break

        for i in range(top, bottom + 1):    #top to bottom
            spiral_result.append(matrix[i][right])
        right -= 1

        if len(matrix) * len(matrix[0]) == len(spiral_result):
            break

        for i in range(right, left - 1, -1):    #right to left
            spiral_result.append(matrix[bottom][i])
        bottom -= 1

        if len(matrix) * len(matrix[0]) == len(spiral_result):
            break

        for i in range(bottom, top - 1, -1):    #bottom to top
            spiral_result.append(matrix[i][left])
        left += 1
    
    return spiral_result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("traversing", matrix, "in a spiral form visits", spiralOrder(matrix), "in this order.")

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("traversing", matrix2, "in a spiral form visits", spiralOrder(matrix2), "in this order.")

matrix3 = [[7],[9],[6]]
print("traversing", matrix3, "in a spiral form visits", spiralOrder(matrix3), "in this order.")