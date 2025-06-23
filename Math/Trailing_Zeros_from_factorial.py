# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:53:10 2025

@author: jwang

Problem Description:
    Given an integer n, return the number of trailing zeroes in n!.
    Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""

def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    divisor = 5
    count_trailing_zeros = 0
    while(n >= divisor):
        count_trailing_zeros += (n // divisor)
        divisor *= 5
    
    return count_trailing_zeros

print(trailingZeroes(3))
print(trailingZeroes(5))
print(trailingZeroes(0))
print(trailingZeroes(25))
print(trailingZeroes(26))
print(trailingZeroes(30))