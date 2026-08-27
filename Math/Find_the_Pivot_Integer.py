"""
Problem Description:
    - Given a positive integer n, find the pivot integer x such that:
        * The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

    - Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot 
    index for the given input.

Constraints:
    - 1 <= n <= 1000
"""

def pivotInteger(n):
    """
    :type n: int
    :rtype: int
    """
    totalSum = (n * (n + 1)) // 2   # sum from 1 to n inclusive

    for num in range(1, n + 1):
        subSum = (num * (num + 1)) // 2
        # check whether the sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
        if subSum == totalSum - subSum + num:
            return num

    return -1    

n = 8
print(pivotInteger(n))  # Output: 6

n2 = 1
print(pivotInteger(n2))  # Output: 1

n3 = 4
print(pivotInteger(n3))  # Output: -1
