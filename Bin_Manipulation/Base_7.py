# -*- coding: utf-8 -*-
"""
Created on Wed May 28 22:50:39 2025

@author: jwang
"""

def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    base_seven = ""
    if num == 0:
        return "0"
    
    start_num = num
    while(abs(num) > 0):
        base_seven = str(abs(num) % 7) + base_seven
        num = abs(num) // 7
    if start_num < 0:
        base_seven = "-" + base_seven
    return base_seven 

print(convertToBase7(0))
print(convertToBase7(10))
print(convertToBase7(13))
print(convertToBase7(14))
print(convertToBase7(17))
print(convertToBase7(100))
print(convertToBase7(200))
print(convertToBase7(-7))