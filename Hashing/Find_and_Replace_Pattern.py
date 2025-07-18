# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 22:36:35 2025

@author: jwang

Problem Description:
    Given a list of strings words and a string pattern, return a list of words[i] 
    that match pattern. You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that 
    after replacing every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: 
    every letter maps to another letter, and no two letters map to the same letter.

Constraints:
    1 <= pattern.length <= 20
    1 <= words.length <= 50
    words[i].length == pattern.length
    pattern and words[i] are lowercase English letters.
"""

def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """

    pattern_matches = []

    for word in words:
        flag = True
        dict_check = dict()
        for i in range(len(word)):
            if word[i] not in dict_check:
                if pattern[i] in dict_check.values():
                    flag = False
                else:
                    dict_check[word[i]] = pattern[i]
            else:
                if dict_check[word[i]] != pattern[i]:
                    flag = False
            
        if flag == True:
            pattern_matches.append(word)
    
    return pattern_matches

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(findAndReplacePattern(words, pattern))    #["mee","aqq"]

words2 = ["a","b","c"]
pattern2 = "a"
print(findAndReplacePattern(words2, pattern2))  #["a","b","c"]
