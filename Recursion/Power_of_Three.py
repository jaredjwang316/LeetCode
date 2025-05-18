# -*- coding: utf-8 -*-
"""
Created on Sun May 18 10:54:42 2025

@author: jwang
"""

def isPowerOfThree( n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    elif n == 1:
        return True
    
    if n % 3 != 0:
        return False
    
    return isPowerOfThree(n // 3)

print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(-1))
print(isPowerOfThree(30))
print(isPowerOfThree(49))