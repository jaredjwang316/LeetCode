# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:51:28 2025

@author: jwang
"""

def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    exp = 0
    for i in range(len(b) - 1, -1, -1):
        exp = exp + b[i] * pow(10, abs(i - (len(b) - 1)))
    
    #use the fast-powering modular algoritm
    result = 1
    while(exp > 0):
        if exp % 2 == 1:
            result = (result * a) % 1337
        a = (a * a) % 1337
        exp = exp // 2
    return result

a = 2
b = [3]
print(superPow(a, b))

a1 = 2
b1 = [1, 0]
print(superPow(a1, b1))

a2 = 1
b2 = [4,3,3,8,5,2]
print(superPow(a2, b2))

a3 = 7
b3 = [4]
print(superPow(a3, b3))