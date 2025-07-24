# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:33:56 2025

@author: jwang

Problem Description:
    - Given two strings s and goal, return true if you can swap two letters in s 
    so the result is equal to goal, otherwise, return false.
    - Swapping letters is defined as taking two indices i and j (0-indexed) such 
    that i != j and swapping the characters at s[i] and s[j]. For example, 
    swapping at indices 0 and 2 in "abcd" results in "cbad".

Constraints:
    1 <= s.length, goal.length <= 2 * 10^4
    s and goal consist of lowercase letters.
"""

def buddyStrings(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    
    if s == goal:   #swapping is possible only if there is at least one character that appears more than once
        letter_freq = dict()
        for ch in s:
            if ch not in letter_freq:
                letter_freq[ch] = 1
            else:
                letter_freq[ch] += 1
        
        for freq in letter_freq.values():
            if freq >= 2:
                return True
        
        return False    #no characters in the string appears more than once
    else:
        discrepancies = []
        indices = []    #indices where chars do not equal
        for i in range( min(len(s), len(goal)) ):
            if s[i] != goal[i]:
                discrepancies.append(s[i])
                indices.append(i)

        if len(discrepancies) != 2: #one swap is not possible to make s equal to goal
            return False

    #if string s and goal are not equal and one swap is possible
    chars_of_s = list(s)
    chars_of_s[indices[1]] = discrepancies[0]
    chars_of_s[indices[0]] = discrepancies[1]    

    s = ""
    for ch in chars_of_s:
        s += ch

    if s == goal:
        return True
    return False    

s = "ab"
goal = "ba"
print(buddyStrings(s, goal))    #True -> You can swap s[0] = 'a' and s[1] = 'b' to get "ba"

s2 = "ab"
goal2 = "ab"
print(buddyStrings(s2, goal2))  #False -> The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

s3 = "aa"
goal3 = "aa"
print(buddyStrings(s3, goal3))  #True -> You can swap s[0] = 'a' and s[1] = 'a' to get "aa
