# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 21:28:41 2025

@author: jwang

Problem Description:
    You are given an integer array deck where deck[i] represents the number 
    written on the ith card.
    Partition the cards into one or more groups such that:
        - Each group has exactly x cards where x > 1, and
        - All the cards in one group have the same integer written on them.
    Return true if such partition is possible, or false otherwise.

Constraints:
    1 <= deck.length <= 10^4
    0 <= deck[i] < 10^4
"""

def findGCD(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    
    while(b != 0):
        temp = a
        a = b
        b = temp % b
    
    if a != 0:
        return a
    return 1

def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    if len(deck) == 1:
        return False
    
    card_freq = dict()
    for d in deck:
        if d not in card_freq:
            card_freq[d] = 1
        else:
            card_freq[d] += 1
    
    freq_list = []
    for freq in card_freq.values():
        freq_list.append(freq)
    
    for i in range(len(freq_list) - 1):
        for j in range(i + 1, len(freq_list)):
            if findGCD(freq_list[i], freq_list[j]) == 1:
                return False
    return True

deck = [1,2,3,4,4,3,2,1]
print(hasGroupsSizeX(deck))     #true

deck2 = [1,1,1,2,2,2,3,3]
print(hasGroupsSizeX(deck2))    #false

deck3 = [1]
print(hasGroupsSizeX(deck3))    #false


