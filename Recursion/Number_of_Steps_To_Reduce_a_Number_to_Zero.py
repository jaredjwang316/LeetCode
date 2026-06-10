"""
Problem Description:
    - Given an integer num, return the number of steps to reduce it to zero.
    - In one step, if the current number is even, you have to divide it by 2, otherwise, you have 
    to subtract 1 from it.

Constraints:
    - 0 <= num <= 10^6
"""

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0:
        return 0
    
    if num % 2 == 0:
        return 1 + numberOfSteps(num // 2)
    
    return 1 + numberOfSteps(num - 1)

num = 14
print(numberOfSteps(num))   # Output: 6

num2 = 123
print(numberOfSteps(num2))  # Output: 12