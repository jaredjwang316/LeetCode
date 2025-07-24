# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 22:45:23 2025

@author: jwang

Problem Description:
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""

def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    count_palin_substrings = 1

    for i in range(1, len(s)):
        #odd-sized substrings
        left = i
        right = i

        while(left >= 0 and right < len(s) and s[left] == s[right]):
            count_palin_substrings += 1
            left -= 1
            right += 1

        #even-sized substrings
        left = i - 1
        right = i
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            count_palin_substrings += 1
            left -= 1
            right += 1
    
    return count_palin_substrings

s = "abc"
print(countSubstrings(s))   #3

s2 = "aaa"
print(countSubstrings(s2))  #6
