# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 10:47:46 2025

@author: jwang

Problem Description:
    A permutation perm of n + 1 integers of all the integers in the range [0, n] 
    can be represented as a string s of length n where:
        s[i] == 'I' if perm[i] < perm[i + 1], and
        s[i] == 'D' if perm[i] > perm[i + 1].
    Given a string s, reconstruct the permutation perm and return it. If there 
    are multiple valid permutations perm, return any of them.

Important Constraints:
    1 <= s.length <= 105
    s[i] is either 'I' or 'D'.
 
"""

def diStringMatch(s):
    """
    :type s: str
    :rtype: List[int]
    """
    
    perm = []
    for i in range(len(s) + 1):
        perm.append(0)
    
    low = 0
    high = len(s)
    for ch in range(len(s)):
        if s[ch] == 'I':
            perm[ch] = low
            low += 1
        else:
            perm[ch] = high
            high -= 1

    for i in range(len(s) + 1):
        if i not in perm:
            perm[len(perm) - 1] = i
            break
    return perm

s = "IDID"
print(diStringMatch(s))

s2 = "III"
print(diStringMatch(s2))

s3 = "DDI"
print(diStringMatch(s3))