# -*- coding: utf-8 -*-
"""
Created on Thu May 15 15:23:26 2025

@author: jwang
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    int_to_roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 
                         40: "XL", 50: "L", 90: "XC", 100: "C",
                         400: "CD", 500: "D", 900: "CM", 1000: "M"}
        
    roman_crit = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_result = ""
    while (num > 0):
        for crit in roman_crit:
            if crit <= num:
                roman_result += int_to_roman_dict[crit]
                num = num - crit
                break
    return roman_result
    
print(intToRoman(1))
print(intToRoman(13))
print(intToRoman(14))
print(intToRoman(58))
print(intToRoman(1994))
print(intToRoman(3749))