# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 23:03:16 2025

@author: jwang

Problem Description:
    Given a signed 32-bit integer x, return x with its digits reversed. If 
    reversing x causes the value to go outside the signed 32-bit integer range 
    [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
    -2^31 <= x <= 2^31 - 1
"""

def extractDigitsInReverse(number):
    rev = ""
    starting_num = number
    if number < 0:
        number *= -1

    while(number > 0):  #reverse digits placement with number slicing technique
        rev = rev + str(number % 10)
        number //= 10
    
    if len(rev) == 10:
        if starting_num > 0 and rev > "2147483647": #upper bound limit if 2^31 - 1
            return 0
        if starting_num < 0 and rev > "2147483648": #lower bound limit is (-1) * 2^31
            return 0
    
    if starting_num < 0:    #need to add a negative sign to reversed integer
        rev = "-" + rev
    return int(rev)

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return x

    return extractDigitsInReverse(x)    

x = 123
print("Reversing the digits of", x, "results in", reverse(x))    #321

x2 = -123
print("Reversing the digits of", x2, "results in", reverse(x2))  #-321

x3 = 120
print("Reversing the digits of", x3, "results in", reverse(x3))  #21

x4 = 1534236469
print("Reversing the digits of", x4, "results in", reverse(x4))  #0

x5 = -1534236469
print("Reversing the digits of", x5, "results in", reverse(x5))  #0


