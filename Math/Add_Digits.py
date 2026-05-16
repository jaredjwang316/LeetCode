"""
Problem Description:
    - Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Constraints:
    - 0 <= num <= 2^31 - 1
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    
    while(num >= 10):
        updated_num = 0
        while(num > 0): #doing the number slicing technique
            updated_num = updated_num + (num % 10)
            num = num // 10
        num = updated_num
        
    return num

num1 = 38
print(addDigits(num1))  #Output: 2

num2 = 0
print(addDigits(num2))  #Output: 0

num3 = 10
print(addDigits(num3))  #Output: 1
