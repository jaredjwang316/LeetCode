"""
Problem Description:
    - Given a positive integer n, write a function that returns the number of set bits in its binary 
    representation (also known as the Hamming weight).

Constraints:
    - 1 <= n <= 2^31 - 1
"""

def countOneBits(n):
    if n == 0:
        return 0
    
    return (n % 2) + countOneBits(n // 2)

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """

    return countOneBits(n)

n = 11
print(hammingWeight(n)) #Output: 3

n2 = 128
print(hammingWeight(n2)) #Output: 1

n3 = 2147483645
print(hammingWeight(n3)) #Output: 30