# -*- coding: utf-8 -*-
"""
Created on Sat May 17 21:57:49 2025

@author: jwang
"""

def convertToBinary(num):
    flipped = ""
    while(num > 0):
        flipped = flipped + str(num % 2)
        num = num // 2
    proper = ""
    for i in range(len(flipped) - 1, -1, -1):
        proper += flipped[i]
    return proper

def binaryToInt(binaryString):
    binToInt = 0
    count = 0
    for i in range(len(binaryString) - 1, -1, -1):
        if binaryString[i] == '1':
            binToInt = binToInt + int(binaryString[i]) * pow(2, count)
        count += 1
    return binToInt

# @param n, an integer
# @return an integer
def reverseBits(n): 
    nBinary = convertToBinary(n)
    while(len(nBinary) < 32):
        nBinary = "0" + nBinary
    rev_bits = ""
    for i in range(len(nBinary) - 1, -1, -1):
        rev_bits += nBinary[i]

    return binaryToInt(rev_bits)

