# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:11:48 2025

@author: jwang

Problem Description:
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:
        Whitespace: Ignore any leading whitespace (" ").
        Signedness: Determine the sign by checking if the next character is '-' 
        or '+', assuming positivity if neither present.
        Conversion: Read the integer by skipping leading zeros until a non-digit 
        character is encountered or the end of the string is reached. If no digits 
        were read, then the result is 0.
        Rounding: If the integer is out of the 32-bit signed integer range 
        [-2^31, 2^31 - 1], then round the integer to remain in the range. 
        Specifically, integers less than -2^31 should be rounded to -2^31, and 
        integers greater than 2^31 - 1 should be rounded to 2^31 - 1.

    Return the integer as the final result.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), 
    digits (0-9), ' ', '+', '-', and '.'.
"""

def checkOverBounds(result):
    #handle rounding: rounding to the integer that remains in the range of [-2^31, 2^31 - 1]
    if result[0] == '-':
        if len(result) > 11:
            return (-1)* int(pow(2, 31))
        elif len(result) == 11:
            if result >= "-2147483648":
                return (-1)* int(pow(2, 31))
    else:
        if len(result) > 10:
            return int(pow(2, 31)) - 1
        elif len(result) == 10:
            if result >= "2147483647":
                return int(pow(2, 31)) - 1
    
    #if there are no overboundary issues
    return int(result)

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.lstrip()  #ignore leading whitespaces
    if s == "":
        return 0
    
    result = ""
    for ch in range(len(s)):
        if ch != 0:
            if s[ch].isdigit() == False:
                #Reading stops at the first non-digit character
                if result != "" and result != '-':
                    return checkOverBounds(result)
                else:   
                    return 0
            elif s[ch] == '0':
                if result == "" or result == '-':    #skip leading zeros
                    continue
                else:
                    result += s[ch]
            elif s[ch].isdigit():
                result += s[ch]
        else:
            if s[ch] == '-':
                result += s[ch]
            elif s[ch] == '0':  #skip leading zeros
                continue
            elif s[ch] == '+':
                continue
            elif s[ch].isdigit():   #if non-zero digit
                result += s[ch]
            else:   #if s[0] is not a digit nor a sign
                return 0
    
    if result == "" or result == '-':
        return 0

    return checkOverBounds(result)

s = "42"
print(myAtoi(s))    #42

s2 = " -042"
print(myAtoi(s2))   #-42 -> leading whitespace and zeros are ignored

s3 = "1337c0d3"
print(myAtoi(s3))   #1337 -> ("1337" is read in; reading stops because the next character is a non-digit)

s4 = "0-1"
print(myAtoi(s4))   #0 -> ("0" is read in; reading stops because the next character is a non-digit)

s5 = "words and 987"
print(myAtoi(s5))   #0 -> Reading stops at the first non-digit character 'w'.

s6 = "-+12"
print(myAtoi(s6))   #0

s7 = "21474836460"
print(myAtoi(s7))   #2147483647 -> reaches upper bound limit of 32-bit signed integer range

s8 = "      -11919730356x"
print(myAtoi(s8))   #-2147483648 -> reaches lower bound limit of 32-bit signed integer range

s9 = "2147483646"
print(myAtoi(s9))   #2147483646

s10 = "-91283472332"
print(myAtoi(s10))  #-2147483648

s11 = "-000000000000001"
print(myAtoi(s11))  #-1