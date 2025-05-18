# -*- coding: utf-8 -*-
"""
Created on Sat May 17 22:08:40 2025

@author: jwang
"""

def convertToBinary(n):
    binary_result = ""
    while(n > 0):
        binary_result = str(n % 2) + binary_result
        n = n // 2
    
    return binary_result

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binary_x = convertToBinary(x)
    binary_y = convertToBinary(y)

    while(len(binary_x) < len(binary_y)):
        binary_x = '0' + binary_x

    while(len(binary_y) < len(binary_x)):
        binary_y = '0' + binary_y

    hamming_distance = 0
    for i in range(len(binary_x)):
        if binary_x[i] != binary_y[i]:
            hamming_distance += 1
    
    return hamming_distance

print(hammingDistance(1, 4))
print(hammingDistance(3, 1))