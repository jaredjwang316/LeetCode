# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:58:17 2025

@author: jwang
"""

def isHappy( n):
    """
    :type n: int
    :rtype: bool
    """

    square_digit_sum = 10
    while(square_digit_sum >= 10):  
        square_digit_sum = 0 #reset it
        while(n > 0):
            square_digit_sum += pow( (n % 10), 2 )
            n = n // 10
        n = square_digit_sum
    
    if square_digit_sum == 1 or square_digit_sum == 7:
        return True
    
    return False

print("Is 19 a happy number?", isHappy(19))
print("Is 2 a happy number?", isHappy(2))
print("Is 1111111 a happy number?", isHappy(1111111))
print("Is 7 a happy number?", isHappy(7))