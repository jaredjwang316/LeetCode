# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 16:44:49 2025

@author: jwang

Problem Description:
    Given a string s, return the longest palindromic substring in s.

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """            
    longest = str(s[0])

    for i in range(1, len(s)):
        #odd-length substrings
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome = s[left:right + 1]
            if len(palindrome) > len(longest):
                longest = palindrome
            left -= 1
            right += 1
        
        #even-length substrings
        left = i - 1
        right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome = s[left:right + 1]
            if len(palindrome) > len(longest):
                longest = palindrome
            left -= 1
            right += 1

    return longest  

s = "babad"
print("The longest palindromic substring in", s, ":", longestPalindrome(s)) #bab

s2 = "cbbd"
print("The longest palindromic substring in", s2, ":", longestPalindrome(s2))   #bb
