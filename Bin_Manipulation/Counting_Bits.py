# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:03:56 2025

@author: jwang
"""

def convertBinary(num):
    if num == 0:
        return "0"
    binary = ""
    while(num > 0):
        binary = str(num % 2) + binary
        num = num // 2

    return binary

def countBits( n):
    """
    :type n: int
    :rtype: List[int]
    """
    count_ones = 0  #count number of ones bit for each binary string
    numOnesList = []
    for i in range(n + 1):
        count_ones = 0  #reset counting variable
        for j in range(len(convertBinary(i))):   #count number of ones in binary representation
            if convertBinary(i)[j] == '1': #if character is 1, not 0
                count_ones += 1 
        numOnesList.append(count_ones)
    return numOnesList

print(countBits(2))
print(countBits(5))