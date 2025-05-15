# -*- coding: utf-8 -*-
"""
Created on Thu May 15 15:27:59 2025

@author: jwang
"""

import math

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:   #special case: 0 and 1 are neither prime nor composite
        return 0

    isPrimeList = []

    for i in range(n):
        isPrimeList.append(True)
        
    isPrimeList[0] = False
    isPrimeList[1] = False

    for i in range(2, int(math.sqrt(n)) + 1 ):
        if isPrimeList[i] == True:
            for j in range(i * i, n, i):
                isPrimeList[j] = False

    count_primes = 0
    for i in range(2, n):
        if isPrimeList[i] == True:
            count_primes += 1

    return count_primes     

print("There are", countPrimes(2), "prime numbers less than 2")
print("There are", countPrimes(10), "prime numbers less than 10")
print("There are", countPrimes(100), "prime numbers less than 100")
