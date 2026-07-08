"""
Problem Description:
    - You are given an integer n.  Form a new integer x by concatenating all the non-zero digits of 
    n in their original order. If there are no non-zero digits, x = 0.
    - Let sum be the sum of digits in x.
    - Return an integer representing the value of x * sum.

Constraints:
    - 0 <= n <= 10^9
"""

def sumAndMultiply(n):
    """
    :type n: int
    :rtype: int
    """
    non_zero_digits = []
    
    while(n > 0):
        if n % 10 != 0:
            non_zero_digits.append(n % 10)
        n = n // 10
    
    if len(non_zero_digits) == 0:   #if there are no non-zero digits
        return 0

    x = 0
    for i in range(len(non_zero_digits)):
        x = x + non_zero_digits[i] * pow(10, i)
    
    return x * sum(non_zero_digits)

n = 10203004
print(sumAndMultiply(n))  # Output: 12340

n2 = 1000
print(sumAndMultiply(n2))  # Output: 1

n3 = 0
print(sumAndMultiply(n3))  # Output: 0