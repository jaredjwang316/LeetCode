# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 14:55:53 2025

@author: jwang
"""

def largeGroupPositions(s):
    """
    :type s: str
    :rtype: List[List[int]]
    """
    if len(s) < 3:
        return []
    
    large_groups = []
    left_index = 0  #starting index of the consecutive groups of characters
    count_consecutive = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count_consecutive += 1
        else:
            if count_consecutive >= 3:  #definition of a large group
                large_groups.append([left_index, i - 1])
            count_consecutive = 1   #reset the count of consecutive characters
            left_index = i
    if count_consecutive >= 3:
        large_groups.append([left_index, len(s) - 1])
    return large_groups  

s = "abbxxxxzzy"
print(largeGroupPositions(s)) 

s2 = "abc"
print(largeGroupPositions(s2))

s3 = "abcdddeeeeaabbbcd"
print(largeGroupPositions(s3))

s4 = "aaa"
print(largeGroupPositions(s4))

s5 = "bbbb"
print(largeGroupPositions(s5))     