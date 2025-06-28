# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:05:56 2025

@author: jwang
"""

def isVowel(ch):
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return True
    
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    
    return False

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    char_s = list(s)    

    low = 0
    high = len(s) - 1
    while(low < high):
        if isVowel(s[low]) == False:
            low += 1
            continue
        if isVowel(s[high]) == False:
            high -= 1
            continue

        temp = s[low]
        char_s[low] = char_s[high]
        char_s[high] = temp

        low += 1
        high -= 1
        
    result = ""
    for ch in char_s:
        result += ch
    return result

print(reverseVowels("IceCreAm"))
print(reverseVowels("leetcode"))