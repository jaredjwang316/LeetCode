"""
Problem Description:
    - Reversing an integer means to reverse all its digits.
        * For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
    - Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 
    equals num. Otherwise return false.

Constraints:
    - 0 <= num <= 10^6
"""

def isSameAfterReversals(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:    #edge case
        return True

    if num % 10 == 0:
        return False    #leading zeros are not retained
    
    return True

num = 526
print(isSameAfterReversals(num))  # Output: True

num2 = 1800
print(isSameAfterReversals(num2))  # Output: False

num3 = 0
print(isSameAfterReversals(num3))  # Output: True