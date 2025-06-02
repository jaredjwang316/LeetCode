# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 19:29:04 2025

@author: jwang
"""

def convertToBinary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while(n > 0):
        binary = str(n % 2) + binary
        n = n // 2
    
    return binary

def binaryGap(n):
    """
    :type n: int
    :rtype: int
    """
    binary_result = convertToBinary(n)
    max_dist = 0
    distance = 1
    for i in range(1, len(binary_result)):
        if binary_result[i] == '0':
            distance += 1
        else:
            max_dist = max(max_dist, distance)
            distance = 1
    
    return max_dist

print(binaryGap(22))
print(binaryGap(8))
print(binaryGap(5))
print(binaryGap(1))