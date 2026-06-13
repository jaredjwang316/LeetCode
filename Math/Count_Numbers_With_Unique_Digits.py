"""
Problem Description:
    - Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.

Constraints:
    - 0 <= n <= 8
"""

def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    
    accumulate = 10 #all single digit numbers have unique digits
    perm = 9    #the first digit can be within 1 - 9, but not 0
    leftover_choices = 9
    for i in range(2, n + 1, 1):
        perm = perm * leftover_choices  #all digits, except first digit can be a 0
        accumulate = accumulate + perm
        leftover_choices -= 1   #this digit is already used
    
    return accumulate

n = 2
print(countNumbersWithUniqueDigits(n))  #91

n = 0
print(countNumbersWithUniqueDigits(n))  #1