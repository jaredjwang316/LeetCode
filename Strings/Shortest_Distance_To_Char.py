# -*- coding: utf-8 -*-
"""
Created on Fri May 30 17:02:01 2025

@author: jwang
"""

def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    char_occurrence = []
    for i in range(len(s)):
        if s[i] == c:
            char_occurrence.append(i)
    char_pos = 0
    shortest_dist = []
    for i in range(len(s)):
        if s[i] == c:
            shortest_dist.append(0)
            char_pos += 1
        else:
            if i < char_occurrence[0]:
                shortest_dist.append(abs(i - char_occurrence[0]) )
            elif i > char_occurrence[len(char_occurrence) - 1]:
                shortest_dist.append(i - char_occurrence[len(char_occurrence) - 1])
            else:
                shortest_dist.append(min(abs(i - char_occurrence[char_pos]), abs(i - char_occurrence[char_pos - 1])))       
    return shortest_dist

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))

s1 = "aaab"
c1 = "b"
print(shortestToChar(s1, c1))