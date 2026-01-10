# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 13:42:25 2025

@author: jwang

Problem Description:
    In an alien language, surprisingly, they also use English lowercase letters, 
    but possibly in a different order. The order of the alphabet is some 
    permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of 
    the alphabet, return true if and only if the given words are sorted 
    lexicographically in this alien language.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
"""

def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    if len(words) == 1:
        return True
    
    alien_dict = dict()
    for o in range(len(order)):
        alien_dict[order[o]] = o + 1
    
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        
        shortest_word = ""                
        if len(words[i]) < len(words[i - 1]):
            shortest_word = words[i]
        else:
            shortest_word = words[i - 1]

        if shortest_word == words[i]:
            for ch in range(len(shortest_word)):
                if alien_dict[shortest_word[ch]] < alien_dict[(words[i - 1])[ch] ]:
                    return False
                elif alien_dict[shortest_word[ch]] > alien_dict[(words[i - 1])[ch] ]:   #the first moment we encountered that words[i - 1] and words[i] is sorted
                    break
                else:
                    if ch == len(shortest_word) - 1:
                        return False    #any character (except the blank character) is greater than a blank character
        else:
            for ch in range(len(shortest_word)):
                if alien_dict[shortest_word[ch]] > alien_dict[(words[i])[ch] ]: #from alien language, words[i - 1] is lexicographically greater than words[i]
                    return False
                elif alien_dict[shortest_word[ch]] < alien_dict[(words[i])[ch] ]:   #words[i - 1] and words[i] is sorted
                    break
                else:
                    if ch == len(shortest_word) - 1:   #words[i - 1] and words[i] is sorted as any character (except the blank character) is greater than a blank character
                        break
    
    return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print("Is", words, "alien sorted given order", order, "?", isAlienSorted(words, order)) #True

words2 = ["word","world","row"]
order2 = "worldabcefghijkmnpqstuvxyz"
print("Is", words2, "alien sorted given order", order2, "?", isAlienSorted(words2, order2)) #False

words3 = ["apple","app"]
order3 = "abcdefghijklmnopqrstuvwxyz"
print("Is", words3, "alien sorted given order", order3, "?", isAlienSorted(words3, order3)) #False

words4 = ["kuvp","q"]
order4 = "ngxlkthsjuoqcpavbfdermiywz"
print("Is", words4, "alien sorted given order", order4, "?", isAlienSorted(words4, order4)) #True

words5 = ["hello","hellob", "helloa"]
order5 = "hlabcdefgijkmnopqrstuvwxyz"
print("Is", words5, "alien sorted given order", order5, "?", isAlienSorted(words5, order5)) #False

words6 = ["app","apple"]
order6 = "abcdefghijklmnopqrstuvwxyz"
print("Is", words6, "alien sorted given order", order6, "?", isAlienSorted(words6, order6)) #True

words7 = ["ab","aa","ac"]
order7 = "abcdefghijklmnopqrstuvwxyz"
print("Is", words7, "alien sorted given order", order7, "?", isAlienSorted(words7, order7)) #False

words8 = ["kruw","ha","q"]
order8 = "zgxlkthsjuoqcpavbfdermiywn"
print("Is", words8, "alien sorted given order", order8, "?", isAlienSorted(words8, order8)) #True
