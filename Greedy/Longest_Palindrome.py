# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:46:15 2025

@author: jwang
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    letter_freq = dict()

    for ch in s:
        if ch not in letter_freq:
            letter_freq[ch] = 1
        else:
            letter_freq[ch] += 1
    
    longest_palin = 0
    for k,v in letter_freq.items():
        if v > 1:
            if v % 2 == 0:
                longest_palin += v
            else:
                longest_palin += (v - 1)
    
    if longest_palin == len(s):
        return longest_palin
    
    return longest_palin + 1    #that one character can be in the middle of the longest palindrome

s0 = "abccccdd"
print("the length of the longest palindrome that can be be built from", s0, "=", longestPalindrome(s0))
s1 = "a"
print("the length of the longest palindrome that can be be built from", s1, "=", longestPalindrome(s1))