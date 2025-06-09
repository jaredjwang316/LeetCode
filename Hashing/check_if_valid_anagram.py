# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:28:43 2025

@author: jwang
"""

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_freq = dict()
    t_freq = dict()

    for ch in s:
        if ch not in s_freq:
            s_freq[ch] = 1
        else:
            s_freq[ch] += 1
    
    for ch in t:
        if ch not in t_freq:
            t_freq[ch] = 1
        else:
            t_freq[ch] += 1
    
    for k,v in t_freq.items():
        if k not in s_freq.keys():
            return False
        else:
            if t_freq[k] != s_freq[k]:
                return False

    for k,v in s_freq.items():
        if k not in t_freq.keys():
            return False
        else:
            if s_freq[k] != t_freq[k]:
                return False        
    return True

s = "anagram"
t = "nagaram"
print("Is", s, "and", t, "anagrams?", isAnagram(s, t))  #true

s2 = "rat"
t2 = "car"
print("Is", s2, "and", t2, "anagrams?", isAnagram(s2, t2))  #false

s3 = "ab"
t3 = "a"
print("Is", s3, "and", t3, "anagram?", isAnagram(s3, t3))   #false