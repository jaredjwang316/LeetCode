# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:11:23 2025

@author: jwang
"""

def firstUniqChar(s):
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
    
    for i in range(len(s)):
        if letter_freq[s[i]] == 1:
            return i
    
    return -1

print("First unique character in leetcode is at index", firstUniqChar("leetcode"))
print("First unique character in loveleetcode is at index", firstUniqChar("loveleetcode"))
print("First unique character in aabb is at index", firstUniqChar("aabb"))