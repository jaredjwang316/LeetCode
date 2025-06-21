# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 10:22:57 2025

@author: jwang
"""

def reverseOnlyLetters(s):
    """
    :type s: str
    :rtype: str
    """
    letter_reversal = []
    for i in range(len(s)):
        if s[i].isalpha() == True:  #if the character is a letter
            letter_reversal.append(' ')
        else:
            letter_reversal.append(s[i])    #keep all non-english letters in their original position
    
    low = 0
    high = len(s) - 1

    while (low <= high):
        if letter_reversal[low] != ' ':
            low += 1
            continue
        if letter_reversal[high] != ' ':
            high -= 1
            continue
        
        letter_reversal[low] = s[high]
        letter_reversal[high] = s[low]
        low += 1
        high -= 1

    result = ""
    for ch in letter_reversal:
        result += ch
    return result

s = "ab-cd"
print("Reversing only letters of", s, "results in", reverseOnlyLetters(s))

s1 = "a-bC-dEf-ghIj"
print("Reversing only letters of", s1, "results in", reverseOnlyLetters(s1))

s2 = "Test1ng-Leet=code-Q!"
print("Reversing only letters of", s2, "results in", reverseOnlyLetters(s2))



