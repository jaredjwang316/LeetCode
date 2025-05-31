# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:26:19 2025

@author: jwang
"""

def isUgly(n):
    """
    :type n: int
    :rtype: bool
    """

    if n <= 0:
        return False
    
    while(n % 2 == 0):
        n = n // 2
    
    while(n % 3 == 0):
        n = n // 3

    while(n % 5 == 0):
        n = n // 5    
    
    if n == 1:  #if all the prime factors of n are 2, 3, or 5
        return True
    
    return False

print("Is 6 an ugly number?", isUgly(6))
print("Is 1 an ugly number?", isUgly(1))
print("Is 14 an ugly number?", isUgly(14))
print("Is 0 an ugly number?", isUgly(0))