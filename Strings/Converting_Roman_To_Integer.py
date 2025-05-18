# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:04:48 2025

@author: jwang
"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    int_result = 0
    while(i < len(s)):
        if s[i:i+2] == "IV":
            int_result += 4
            i += 2
            continue
        elif s[i:i+2] == "IX":
            int_result += 9
            i += 2
            continue
        elif s[i:i+2] == "XL":
            int_result += 40
            i += 2
            continue
        elif s[i:i+2] == "XC":
            int_result += 90
            i += 2
            continue
        elif s[i:i+2] == "CD":
            int_result += 400
            i += 2
            continue
        elif s[i:i+2] == "CM":
            int_result += 900
            i += 2
            continue
        
        if s[i] == 'I':
            int_result += 1
        elif s[i] == 'V':
            int_result += 5
        elif s[i] == 'X':
            int_result += 10
        elif s[i] == 'L':
            int_result += 50
        elif s[i] == 'C':
            int_result += 100
        elif s[i] == 'D':
            int_result += 500
        else:
            int_result += 1000
        i = i + 1
    
    return int_result

print("III:", romanToInt("III"))
print("LVIII: ", romanToInt("LVIII"))
print("MCMXCIV: ", romanToInt("MCMXCIV"))