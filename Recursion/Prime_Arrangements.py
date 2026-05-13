"""
Problem Description:
    - Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
    - (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product 
    of two positive integers both smaller than it.)
    - Since the answer may be large, return the answer modulo 10^9 + 7.

Constraints:
    - 1 <= n <= 100
"""
from math import sqrt

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)
def numPrimeArrangements(n):
    primes = []
    for i in range(n + 1):
        primes.append(True)
    #0 and 1 are neither prime nor composite
    primes[0] = False
    primes[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] != False:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    
    count_primes = 0
    non_primes = 0
    for i in range(1, len(primes)):
        if primes[i] == True:
            count_primes += 1
        else:
            non_primes += 1
    
    return ( factorial(count_primes) * factorial(non_primes) ) % (pow(10, 9) + 7)

n = 5
print(numPrimeArrangements(n)) # 12

n2 = 100
print(numPrimeArrangements(n2)) # 682289015

n3 = 1
print(numPrimeArrangements(n3)) # 1