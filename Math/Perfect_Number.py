# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:16:18 2025

@author: jwang
"""

import math 

def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 1:    #edge case: the only integer that divides 1 is 1
        return False
    divisor_sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_sum = divisor_sum + i + (num // i)
    
    if divisor_sum == num:
        return True
    return False

print("Is 28 a perfect number?", checkPerfectNumber(28))
print("Is 7 a perfect number?", checkPerfectNumber(7))
print("Is 1 a perfect number?", checkPerfectNumber(1))