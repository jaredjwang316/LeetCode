# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:52:28 2025

@author: jwang
"""

def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """

    if len(s) < 10:
        return []
    
    unique_ten_letter_seq = set()

    repeats = list()
    for i in range(len(s) - 9):
        if s[i: i + 10] not in unique_ten_letter_seq:
            unique_ten_letter_seq.add(s[i: i + 10])
        else:
            if s[i: i + 10] not in repeats:
                repeats.append(s[i: i + 10])
    
    return repeats

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
