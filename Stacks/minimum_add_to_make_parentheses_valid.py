# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:11:46 2025

@author: jwang

Problem Description:
    A parentheses string is valid if and only if:
        - It is the empty string, or
        - It can be written as AB (A concatenated with B), where A and B are valid strings, or
        - It can be written as (A), where A is a valid string.
    You are given a parentheses string s. In one move, you can insert a parenthesis 
    at any position of the string.
        - For example, if s = "()))", you can insert an opening parenthesis to 
        be "(()))" or a closing parenthesis to be "())))".
    Return the minimum number of moves required to make s valid.
"""

def minAddToMakeValid(s):
    """
    :type s: str
    :rtype: int
    """
    
    theStack = []
    for ch in s:
        if ch == '(':
            theStack.append(ch)
        else:
            if len(theStack) != 0:
                if theStack[len(theStack) - 1] == '(':
                    theStack.pop()
                    continue
            theStack.append(')')
    
    return len(theStack)

s = "())"
print(minAddToMakeValid(s))     #1

s2 = "((("
print(minAddToMakeValid(s2))    #3

s3 = "()))(("
print(minAddToMakeValid(s3))    #4