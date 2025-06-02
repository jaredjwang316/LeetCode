# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 14:54:13 2025

@author: jwang
"""

def rotateString(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if len(goal) != len(s):  
        return False
    concatenate = s + s
    if goal in concatenate:
        return True
    return False

s = "abcde"
goal = "cdeab"

print(rotateString(s, goal))

s2 = "abcde"
goal2 = "abced"
print(rotateString(s2, goal2))
