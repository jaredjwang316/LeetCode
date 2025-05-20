# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:19:37 2025

@author: jwang
"""

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    s_ch = dict()

    for ch in s:
        if ch not in s_ch:
            s_ch[ch] = 1
        else:
            s_ch[ch] += 1
    
    t_ch = dict()
    for ch in t:
        if ch not in s_ch:
            return ch
        
        if ch not in t_ch:
            t_ch[ch] = 1
        else:
            t_ch[ch] += 1
            if t_ch[ch] > s_ch[ch]:
                return ch
    
    return s[0] 

print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))
print(findTheDifference("a", "aa"))