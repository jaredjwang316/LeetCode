# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 22:33:30 2025

@author: jwang

Problem Description:
    Given a string s, find the length of the longest without duplicate characters.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    maxLen = 1

    for i in range(len(s) - 1):
        unique_chars = [s[i]]
        for j in range(i + 1, len(s)):
            if s[j] not in unique_chars:
                unique_chars.append(s[j])
                maxLen = max(maxLen, len(unique_chars))
            else:
                break
    
    return maxLen

s = "abcabcbb"
print(lengthOfLongestSubstring(s))  #3 -> abc

s2 = "bbbbb"
print(lengthOfLongestSubstring(s2)) #1 -> b

s3 = "pwwkew"
print(lengthOfLongestSubstring(s3)) #3 -> wke

s4 = ""
print(lengthOfLongestSubstring(s4)) #0
