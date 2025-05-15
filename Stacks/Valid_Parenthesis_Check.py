# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:34:04 2025

@author: jwang
"""

def isValidParenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 1: #all braces, brackets, and parenthesis must go in pairs, where each pair has 2 characters
        return False
        
    theStack = []   #stack contains all opening parts of braces, brackets, and parenthesis
        
    for i in range(len(s)):
        if s[i] == '(':
            theStack.append('(')
        elif s[i] == '[':
            theStack.append('[')
        elif s[i] == '{':
            theStack.append('{')
        elif s[i] == ']':
            if len(theStack) == 0:
                return False
            if theStack[len(theStack) - 1] == '(' or theStack[len(theStack) - 1] == '{':    #unfit opening
                return False
            theStack.pop()
        elif s[i] == ')':
            if len(theStack) == 0:
                return False
            if theStack[len(theStack) - 1] == '[' or theStack[len(theStack) - 1] == '{':    #unfit opening
                return False
            theStack.pop()
        elif s[i] == '}':
            if len(theStack) == 0:
                return False
            if theStack[len(theStack) - 1] == '[' or theStack[len(theStack) - 1] == '(':    #unfit opening
                return False                
            theStack.pop()
        
    if len(theStack) > 0:
        return False
        
    return True

print(isValidParenthesis("()"))
print(isValidParenthesis("()[]{}"))
print(isValidParenthesis("(]"))
print(isValidParenthesis("([])"))
print(isValidParenthesis("([)]"))