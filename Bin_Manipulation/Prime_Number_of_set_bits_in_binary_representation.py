# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 09:17:32 2025

@author: jwang

Problem Description:
    Given two integers left and right, return the count of numbers in the 
    inclusive range [left, right] having a prime number of set bits in their 
    binary representation.

    Recall that the number of set bits an integer has is the number of 1's present 
    when written in binary.For example, 21 written in binary is 10101, which has 3 set bits.

Constraints: 
    1 <= left <= right <= 10^6
    0 <= right - left <= 10^4
"""

import math

def checkIfPrime(num):
    if num == 0 or num == 1:    #Special Case: 0 and 1 are neither prime nor composite
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def convertToBinary(num):
    binary_form = ""
    while(num > 0):
        binary_form = str(num % 2) + binary_form
        num = num // 2
    return binary_form

def countPrimeSetBits(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """

    count_prime_number_of_set_bits = 0
    for i in range(left, right + 1):
        binary_form = convertToBinary(i)
        count_set_bits = 0
        for ch in binary_form:
            if ch == '1':
                count_set_bits += 1
        
        if checkIfPrime(count_set_bits) == True:
            count_prime_number_of_set_bits += 1
    
    return count_prime_number_of_set_bits

left = 6
right = 10
print(countPrimeSetBits(left, right), "numbers have a prime number of set bits")   #4

left2 = 10
right2 = 15
print(countPrimeSetBits(left2, right2), "numbers have a prime number of set bits") #5