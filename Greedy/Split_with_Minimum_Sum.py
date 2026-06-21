"""
Problem Description:
    - Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
        * The concatenation of num1 and num2 is a permutation of num.  In other words, the sum of the number of 
        occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
        * num1 and num2 can contain leading zeros.

    - Return the minimum possible sum of num1 and num2.
    - Notes:
        * It is guaranteed that num does not contain any leading zeros.
        * The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

Constraints:
    - 10 <= num <= 10^9
"""

def splitNum(num):
    """
    :type num: int
    :rtype: int
    """
    str_num = str(num)
    str_num = sorted(str_num)

    num1 = ""
    num2 = ""

    for i in range(len(str_num)):
        if i % 2 == 0:
            num1 += str_num[i]
        else:
            num2 += str_num[i]
    
    return int(num1) + int(num2)

num = 4325
print(splitNum(num))    # Output: 59

num2 = 687
print(splitNum(num2))   # Output: 75