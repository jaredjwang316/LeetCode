# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:54:51 2025

@author: jwang
"""

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    letter_mapping = dict()

    for i in range(len(s)):
        if s[i] not in letter_mapping:
            if t[i] in letter_mapping.values(): #No two characters may map to the same character
                return False
            letter_mapping[s[i]] = t[i]
        else:
            if letter_mapping[s[i]] != t[i]:    #No two characters may map to the same character
                return False

    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
print(isIsomorphic("bad", "bab"))