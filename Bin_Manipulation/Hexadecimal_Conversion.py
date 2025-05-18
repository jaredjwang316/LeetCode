# -*- coding: utf-8 -*-
"""
Created on Sat May 17 22:08:41 2025

@author: jwang
"""

def hexDivision(num):
    hex_result = ""
    hex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
        8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15:'f' 
    }

    while (num > 0):
        hex_result = hex_dict[num % 16] + hex_result
        num = num // 16        
    return hex_result

def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "0"
    
    if num > 0:
        return hexDivision(num)
    else:
        num += pow(2, 32)
    return hexDivision(num)

print("26 converted to hexadecimal is", toHex(26))
print("16 converted to hexadecimal is", toHex(16))
print("-1 converted to hexadecimal is", toHex(-1))