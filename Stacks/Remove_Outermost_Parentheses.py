# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 10:32:04 2025

@author: jwang

Problem Description:
    - A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
    where A and B are valid parentheses strings, and + represents string concatenation.
        * For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
    - A valid parentheses string s is primitive if it is nonempty, and there does 
    not exist a way to split it into s = A + B, with A and B nonempty valid 
    parentheses strings.
    - Given a valid parentheses string s, consider its primitive decomposition: 
        s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
    - Return s after removing the outermost parentheses of every primitive string 
    in the primitive decomposition of s.

Constraints:
    1 <= s.length <= 10^5
    s[i] is either '(' or ')'.
    s is a valid parentheses string.
"""

def removeOuterParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    
    aStack = []
    result = ""
    for ch in s:
        if ch == '(':   
            if len(aStack) != 0:    #we are in inner parentheses
                result += ch
            aStack.append('(')
        else:
            if len(aStack) > 1:
                result += ch
            aStack.pop()
    
    return result

s = "(()())(())"
print("Removing the outer parentheses of", s, "results in", removeOuterParentheses(s))  #()()()

s2 = "(()())(())(()(()))"
print("Removing the outer parentheses of", s2, "results in", removeOuterParentheses(s2))    #()()()()(())

s3 = "()()"
print("Removing the outer parentheses of", s3, "results in", removeOuterParentheses(s3))    #empty string