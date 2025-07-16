# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 11:30:37 2025

@author: jwang

Problem Description:
    In English, we have a concept called root, which can be followed by some 
    other word to form another longer word - let's call this word derivative. 
    For example, when the root "help" is followed by the word "ful", we can 
    form a derivative "helpful".
    
    Given a dictionary consisting of many roots and a sentence consisting of words 
    separated by spaces, replace all the derivatives in the sentence with the 
    root forming it. If a derivative can be replaced by more than one root, 
    replace it with the root that has the shortest length.
    
    Return the sentence after the replacement.

Constraints:
    
    1 <= dictionary.length <= 1000
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case letters.
    1 <= sentence.length <= 10^6
    sentence consists of only lower-case letters and spaces.
    The number of words in sentence is in the range [1, 1000]
    The length of each word in sentence is in the range [1, 1000]
    Every two consecutive words in sentence will be separated by exactly one space.
    sentence does not have leading or trailing spaces.
"""

def replaceWords(dictionary, sentence):
    """
    :type dictionary: List[str]
    :type sentence: str
    :rtype: str
    """
    words = sentence.split(' ')
    
    for w in range(len(words)):
        shortest_root = pow(2, 31) - 1
        shortest_root_word = ""
        for dict_word in dictionary:
            if dict_word == (words[w])[0:len(dict_word)]:   #starting part of the word (derivative) matches the root
                shortest_root_word = dict_word
                if len(dict_word) < shortest_root:
                    shortest_root = len(dict_word)
                    shortest_root_word = dict_word
                words[w] = shortest_root_word   #replace that derivative with the root with the shortest length
                
                
    result = ""
    for w in words:
        result = result + w + " "
    result = result[0:len(result) - 1]    #remove the last white space
    return result
                
                
    result = ""
    for w in words:
        result = result + w + " "
    result = result[0:len(result) - 1]    #remove the last white space
    return result

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))   # "the cat was rat by the bat"

dictionary2 = ["a","b","c"]
sentence2 = "aadsfasf absbs bbab cadsfafs"
print(replaceWords(dictionary2, sentence2))     # "a a b c"

dictionary3 = ["catt","cat","bat","rat"]
sentence3 = "the cattle was rattled by the battery"
print(replaceWords(dictionary3, sentence3)) # "the cat was rat by the bat"

dictionary4 = ["cat","catt","bat","rat"]
sentence4 = "the cattle was rattled by the battery"
print(replaceWords(dictionary4, sentence4)) # "the cat was rat by the bat"