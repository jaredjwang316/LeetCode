# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 09:28:58 2025

@author: jwang

Problem Description:
    You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill:
        - Begin with the starting pixel and change its color to color.
        - Perform the same process for each pixel that is directly adjacent 
          (pixels that share a side with the original pixel, either horizontally 
           or vertically) and shares the same color as the starting pixel.
        - Keep repeating this process by checking neighboring pixels of the 
          updated pixels and modifying their color if it matches the original 
          color of the starting pixel.
        - The process stops when there are no more adjacent pixels of the 
          original color to update.

    Return the modified image after performing the flood fill.

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 2^16
    0 <= sr < m
    0 <= sc < n
"""

def floodFill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    
    start_color = image[sr][sc]
    def spiralOut(image, row, col, color):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[row]):   #if out of boundary
            return

        if image[row][col] != start_color:  # if that pixel's color does not match with the original color of the starting pixel.
            return
        
        image[row][col] = color     #updated pixels and modifying their color if it matches the original color of the starting pixel.
        spiralOut(image, row - 1, col, color)   #up
        spiralOut(image, row + 1, col, color)   #down
        spiralOut(image, row, col - 1, color)   #left
        spiralOut(image, row, col + 1, color)   #down
    
    if start_color != color:    #if the starting pixel is not already colored with color
        spiralOut(image, sr, sc, color)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]] 
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))

image2 = [[0,0,0],[0,0,0]]
sr2 = 0
sc2 = 0
color2 = 0
print(floodFill(image2, sr2, sc2, color2))