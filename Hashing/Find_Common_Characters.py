# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 16:11:52 2025

@author: jwang

Problem Description:
    Given a string array words, return an array of all characters that show up 
    in all strings within the words (including duplicates). You may return the 
    answer in any order.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""

def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    if len(words) == 1:
        return list(words[0])
    
    common_chars = list(words[0])
    result = []
    for w in range(1, len(words)):
        result = []
        for ch in words[w]:
            if ch in common_chars:
                result.append(ch)
                common_chars.remove(ch) #avoid counting the same thing twice
        
        common_chars = result
    
    return result

words = ["bella","label","roller"]
print(commonChars(words))   #[l, l, e]

words2 = ["cool","lock","cook"]
print(commonChars(words2))  #[c, o]

words3 = ["cool"]
print(commonChars(words3))  #[c, o, o, l]
