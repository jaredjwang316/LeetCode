# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 18:39:59 2025

@author: jwang

Problem Description:
    Given two strings ransomNote and magazine, return true if ransomNote can be 
    constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
"""

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    ransomNote_letters_freq = dict()
    magazine_letters_freq = dict()

    for ch in ransomNote:
        if ch not in ransomNote_letters_freq:
            ransomNote_letters_freq[ch] = 1
        else:
            ransomNote_letters_freq[ch] += 1

    for ch in magazine:
        if ch not in magazine_letters_freq:
            magazine_letters_freq[ch] = 1
        else:
            magazine_letters_freq[ch] += 1       

    for k,v in ransomNote_letters_freq.items():
        if k not in magazine_letters_freq.keys():   #that letter does not exist in magazine
            return False
        else:
            if ransomNote_letters_freq[k] > magazine_letters_freq[k]:
                return False    #each letter in magazine can only be used once in ransomNote
    
    return True

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))

ransomNote2 = "aa"
magazine2 = "ab"
print(canConstruct(ransomNote2, magazine2))

ransomNote3 = "aa"
magazine3 = "aab"
print(canConstruct(ransomNote3, magazine3))

ransomNote4 = "aab"
magazine4 = "baa"
print(canConstruct(ransomNote4, magazine4))