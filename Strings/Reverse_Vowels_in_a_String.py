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

    resulting_chars = []
    vowel_indices = []
    theVowels = []

    for i in range(len(s)):
        if isVowel(s[i]):
            vowel_indices.append(i)
            theVowels.append(s[i])
            resulting_chars.append(' ')
        else:
            resulting_chars.append(s[i])
    left = 0
    right = len(vowel_indices) - 1

    while (left < right):
        temp = vowel_indices[left]
        vowel_indices[left] = vowel_indices[right]
        vowel_indices[right] = temp

        left += 1
        right -= 1
    for i in range(len(vowel_indices)):
        resulting_chars[vowel_indices[i]] = theVowels[i]
    
    final_string = ""
    for ch in resulting_chars:
        final_string += ch
    
    return final_string

print(reverseVowels("IceCreAm"))
print(reverseVowels("leetcode"))