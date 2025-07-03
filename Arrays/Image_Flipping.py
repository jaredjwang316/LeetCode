# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 12:10:08 2025

@author: jwang

Problem Description:
    Given an n x n binary matrix image, flip the image horizontally, then invert 
    it, and return the resulting image.
    To flip an image horizontally means that each row of the image is reversed.
        - For example, flipping [1,1,0] horizontally results in [0,1,1].
    To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
        - For example, inverting [0,1,1] results in [1,0,0].

Constraints:
    n == image.length
    n == image[i].length
    1 <= n <= 20
    images[i][j] is either 0 or 1.
"""

def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """

    #reverse the rows
    for r in range(len(image)):
        for c in range(len(image[r]) // 2):
            temp = image[r][c]
            image[r][c] = image[r][len(image[r]) - c - 1]
            image[r][len(image[r]) - c - 1] = temp
    
    #invert the image
    for r in range(len(image)):
        for c in range(len(image[r])):
            if image[r][c] == 0:
                image[r][c] = 1
            else:
                image[r][c] = 0
    
    return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print("Original Image:", image)
print("After flipping and inverting the image:", flipAndInvertImage(image))

image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print("Original Image:", image2)
print("After flipping and inverting the image:", flipAndInvertImage(image2))

