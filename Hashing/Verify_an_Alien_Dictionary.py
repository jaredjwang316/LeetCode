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
    alien_order = dict()
    
    for i in range(len(order)):
        alien_order[order[i]] = i + 1   #index represents the order of the alphabet in the alien dictionary

    shortest_comp = ""
    for w in range(1, len(words)):
        if words[w] == words[w - 1]:
            continue
        flag = False
        if len(words[w]) <= len(words[w - 1]):
            shortest_comp = words[w]
        else:
            shortest_comp = words[w - 1]
        
        if shortest_comp == words[w - 1]:
            for ch in range(len(shortest_comp)):
                if alien_order[ shortest_comp[ch] ] < alien_order[ (words[w])[ch] ]:
                    flag = True
                elif alien_order[ shortest_comp[ch] ] > alien_order[ (words[w])[ch] ]:
                    if not flag:
                        return False 
                else:
                    if ch == len(shortest_comp) - 1:
                        continue
        else:
            for ch in range(len(shortest_comp)):
                if alien_order[ shortest_comp[ch] ] > alien_order[ (words[w - 1])[ch] ]:
                    flag = True
                elif alien_order[ shortest_comp[ch] ] < alien_order[ (words[w - 1])[ch] ]:
                    if not flag:
                        return False 
                else:
                    if ch == len(shortest_comp) - 1:
                        return False                

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
