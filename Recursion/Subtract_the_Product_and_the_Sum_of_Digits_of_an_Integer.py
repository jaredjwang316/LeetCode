"""
Problem Description:
    - Given an integer number n, return the difference between the product of its digits and the 
    sum of its digits. 

Constraints:
    - 1 <= n <= 10^5
"""

def productRecursion(num):
    if num == 0:
        return 1
    return (num % 10) * productRecursion(num // 10)

def sumRecursion(num):
    if num == 0:
        return 0
    return (num % 10) + sumRecursion(num // 10)

def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """

    return productRecursion(n) - sumRecursion(n)

print(subtractProductAndSum(234))   #(2*3*4) - (2+3+4) = 24 - 9 = 15
print(subtractProductAndSum(4421))  #(4*4*2*1) - (4+4+2+1) = 32 - 11 = 21