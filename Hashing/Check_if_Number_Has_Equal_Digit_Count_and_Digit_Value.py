"""
Problem Description:
    - You are given a 0-indexed string num of length n consisting of digits.
    - Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times 
    in num, otherwise return false.

Constraints:
    - n == num.length
    - 1 <= n <= 10
    - num consists of digits.
"""

def digitCount(num):
    """
    :type num: str
    :rtype: bool
    """
    digit_freq = dict()
    
    for i in range(len(num)):
        if ord(num[i]) - 48 not in digit_freq:
            digit_freq[ord(num[i]) - 48] = 1
        else:
            digit_freq[ord(num[i]) - 48] += 1

    for i in range(len(num)):
        if i not in digit_freq: #if digit i occurs zero times in num
            if num[i] != '0':
                return False
        else:
            if digit_freq[i] != ord(num[i]) - 48:    #if occurrence of i not equal to num[i]
                return False
    return True

num = "1210"
print(digitCount(num)) # Output: True

num2 = "030"
print(digitCount(num2)) # Output: False