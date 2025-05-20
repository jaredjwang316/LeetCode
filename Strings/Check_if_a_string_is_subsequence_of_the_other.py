# -*- coding: utf-8 -*-
"""
Created on Mon May 19 23:24:59 2025

@author: jwang
"""

def isSubsequence(s, t):
    i = 0
    j = 0

    while(i < len(s) and j < len(t)):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    if i == len(s):
        return True
    return False

s0 = "abc"
t0 = "ahbgdc"

if isSubsequence(s0, t0) == True:
    print(s0, "is a subsequence of", t0)
else:
    print(s0, "is not a subsequence of", t0)
    
s1 = "axc"
t1 = "ahbgdc"
if isSubsequence(s1, t1) == True:
    print(s1, "is a subsequence of", t1)
else:
    print(s1, "is not a subsequence of", t1)