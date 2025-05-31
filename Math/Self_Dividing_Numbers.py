# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:34:38 2025

@author: jwang
"""

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    self_dividing_nums = []
    flag = True
    for num in range(left, right + 1):
        flag = True
        str_num = str(num)
        if "0" in str_num:  #a self-diving number cannot contain the digit 0
            continue
        for digit in str_num:
            if num % int(digit) != 0: 
                flag = False
        
        if flag == True:
            self_dividing_nums.append(num)
    
    return self_dividing_nums

left = 1
right = 22
print("The self dividing numbers in the given range of", left, 
      "to", right, "inclusive is", selfDividingNumbers(left, right))

left1 = 47
right1 = 85
print("The self dividing numbers in the given range of", left1, 
      "to", right1, "inclusive is", selfDividingNumbers(left1, right1))