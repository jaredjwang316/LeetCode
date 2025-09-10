# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 22:41:22 2025

@author: jwang

Given a valid parentheses string s, return the nesting depth of s. The nesting 
depth is the maximum number of nested parentheses.

Constraints:
    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.
"""

def maxDepth(s):
    """
    :type s: str
    :rtype: int
    """
    max_nested_parentheses = 0
    parentheses_stack = []
    for i in range(len(s)):
        if s[i] == '(':
            parentheses_stack.append('(')
        elif s[i] == ')':
            max_nested_parentheses = max(max_nested_parentheses, len(parentheses_stack))
            parentheses_stack.pop()
    
    return max_nested_parentheses

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))  #3,  because digit 8 is inside of 3 nested parentheses

s2 = "(1)+((2))+(((3)))"
print(maxDepth(s2)) #3, because digit 3 is inside of 3 nested parentheses

s3 = "()(())((()()))"
print(maxDepth(s3)) #3
