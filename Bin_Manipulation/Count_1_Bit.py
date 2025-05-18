# -*- coding: utf-8 -*-
"""
Created on Sat May 17 22:08:39 2025

@author: jwang
"""

def convertToBinary(n):
    binary_result = ""
    while(n > 0):
        binary_result = str(n % 2) + binary_result
        n = n // 2
    
    return binary_result

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    binary_n = convertToBinary(n)
    count_ones = 0
    for ch in binary_n:
        if ch == '1':
            count_ones += 1
    return count_ones


print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))