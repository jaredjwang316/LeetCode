# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:25:46 2025

@author: jwang
"""

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) > len(haystack): #big never fits into small
        return -1
    
    for i in range(len(haystack) - len(needle) + 1):
        if needle == haystack[i: i + len(needle)]:
            return i
    
    return -1   #needle not part of haystack

print(strStr("sadbutsad", "sad"))
print(strStr("badbutsad", "sad"))
print(strStr("sad", "sadbutsad"))
print(strStr("leetcode", "leet"))
print(strStr("leetcode", "leeto"))