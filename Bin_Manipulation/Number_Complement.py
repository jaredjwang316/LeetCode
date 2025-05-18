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

def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    binary_num = convertToBinary(num)

    number_complement = ""
    for b in binary_num:
        if b == '0':
            number_complement += '1'
        else:
            number_complement += '0'

    result = 0
    for i in range(len(number_complement) - 1, -1, -1):
        if number_complement[i] == '1':
            result += pow(2, (len(number_complement) - i - 1))
    
    return result

print(findComplement(5))
print(findComplement(1))