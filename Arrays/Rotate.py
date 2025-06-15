# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 22:49:11 2025

@author: jwang

Problem Description:
    You are given an n x n 2D matrix representing an image, rotate the 
    image by 90 degrees (clockwise).
    Note: You have to rotate the image in-place, which means you have to modify 
    the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.   

"""

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    #transpose the matrix first
    for r in range(len(matrix)):
        for c in range(r, len(matrix[r])):
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp

    #reverse every row
    for r in range(len(matrix)):
        for c in range(len(matrix[r]) // 2):
            temp = matrix[r][c]
            matrix[r][c] = matrix[r][len(matrix[r]) - 1 - c]
            matrix[r][len(matrix[r]) - 1 - c] = temp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Initial matrix before rotating:", matrix)
rotate(matrix)
print("Resulting matrix after rotating 90 degrees clockwise:", matrix)

print()

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("Initial matrix before rotating:", matrix2)
rotate(matrix2)
print("Resulting matrix after rotating 90 degrees clockwise:", matrix2)
