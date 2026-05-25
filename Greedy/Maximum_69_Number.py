"""
Problem Description:
    - You are given a positive integer num consisting only of digits 6 and 9.
    - Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Constraints:
    - 1 <= num <= 10^4
    - num consists of only 6 and 9 digits.
"""

def maximum69Number (num):
    """
    :type num: int
    :rtype: int
    """
    str_num = list(str(num))
    for i in range(len(str_num)):
        if str_num[i] == '6':
            str_num[i] = '9'
            break
    
    return int("".join(str_num))

num = 9669
print(maximum69Number(num)) #Output: 9969

num2 = 9996
print(maximum69Number(num2)) #Output: 9999

num3 = 9999
print(maximum69Number(num3)) #Output: 9999 - It is better not to apply any change here