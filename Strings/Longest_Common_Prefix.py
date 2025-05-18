# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:18:40 2025

@author: jwang
"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest_word_length = 0
    longest_word = ""
    for word in strs:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word = word
    
    shortest_word_length = longest_word_length
    for word in strs:
        if len(word) < shortest_word_length:
            shortest_word_length = len(word)
    
    longest_common_prefix = ""
    #longest common prefix can at most be equal to the shortest word length in the strs list
    for i in range(shortest_word_length):
        for word in strs:
            if word[i] != longest_word[i]:
                return longest_common_prefix
        longest_common_prefix += longest_word[i]

    return longest_common_prefix

strs = ["flower","flow","flight"]
print("longest common prefix in", strs, "is", longestCommonPrefix(strs))

strs2 = ["dog","racecar","car"]
if longestCommonPrefix(strs2) == "":
    print("longest common prefix in", strs2, "is an empty string")
else:
    print("longest common prefix in", strs2, "is", longestCommonPrefix(strs2))