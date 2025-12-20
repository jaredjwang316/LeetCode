# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 13:31:19 2025

@author: jwang
"""

"""
Problem Description:
    Given two strings s and t, return true if they are equal when both are 
    typed into empty text editors. '#' means a backspace character.

    Note: that after backspacing an empty text, the text will continue empty.

Important Constraints:
    s and t only contain lowercase letters and '#' characters.
"""

def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    stackS = []
    for ch in s:
        if ord(ch) >= 97 and ord(ch) <= 122:
            stackS.append(ch)
        else:
            if len(stackS) > 0:
                stackS.pop()
    
    stackT = []
    for ch in t:
        if ord(ch) >= 97 and ord(ch) <= 122:
            stackT.append(ch)
        else:
            if len(stackT) > 0:
                stackT.pop()   

    if len(stackS) != len(stackT):
        return False
    
    for i in range(len(stackS)):
        if stackS[i] != stackT[i]:
            return False

    return True

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))   #True: Both s and t become "ac".

s2 = "ab##"
t2 = "c#d#"
print(backspaceCompare(s2, t2))     #True: Both s and t become empty strings.

s3 = "a#c"
t3 = "b"
print(backspaceCompare(s3, t3))    #False: s becomes "c" while t becomes "b". 

s4 = "a#c"
t4 = "c"
print(backspaceCompare(s4, t4)) #True: Both s and t become "c".

s5 = ""
t5 = "##"
print(backspaceCompare(s5, t5)) #True: Both s and t become empty strings
