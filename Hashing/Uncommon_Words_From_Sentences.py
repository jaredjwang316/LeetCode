# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 11:46:00 2025

@author: jwang

Problem Description:
    A word is uncommon if it appears exactly once in one of the sentences, 
    and does not appear in the other sentence.
    Given two sentences s1 and s2, return a list of all the uncommon words. 
    You may return the answer in any order.

Constraints:
    1 <= s1.length, s2.length <= 200
    s1 and s2 consist of lowercase English letters and spaces.
    s1 and s2 do not have leading or trailing spaces.
    All the words in s1 and s2 are separated by a single space.
"""


def uncommonFromSentences(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: List[str]
    """
    words_s1 = s1.split(" ")
    words_s2 = s2.split(" ")

    s1_word_freq = dict()
    for w in words_s1:
        if w not in s1_word_freq:
            s1_word_freq[w] = 1
        else:
            s1_word_freq[w] += 1

    s2_word_freq = dict()
    for w in words_s2:
        if w not in s2_word_freq:
            s2_word_freq[w] = 1
        else:
            s2_word_freq[w] += 1
    
    uncommon_words = []
    for k,v in s1_word_freq.items():
        #A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
        if v == 1 and k not in s2_word_freq.keys(): 
            uncommon_words.append(k)
    
    for k,v in s2_word_freq.items():
        #A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
        if v == 1 and k not in s1_word_freq.keys():
            uncommon_words.append(k)

    return uncommon_words

s1 = "this apple is sweet"
s2 = "this apple is sour"
print("List of uncommon words", uncommonFromSentences(s1, s2))

s3 = "apple apple"
s4 = "banana"
print("List of uncommon words:", uncommonFromSentences(s3, s4))
