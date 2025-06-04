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
    resulting_s_list = []
    for ch in s:
        if ch != '#':
            resulting_s_list.append(ch)
        else:   #in this case, based on the given constraint, the character can only be #
            if len(resulting_s_list) > 0:
                resulting_s_list.pop()  #perform backspace operation

    resulting_t_list = [] 
    for ch in t:
        if ch != '#':
            resulting_t_list.append(ch)
        else:   #in this case, based on the given constraint, the character can only be #
            if len(resulting_t_list) > 0:
                resulting_t_list.pop()  #perform backspace operation
    
    resulting_s = ""
    resulting_t = ""
    for ch in resulting_s_list:
        resulting_s += ch
    
    for ch in resulting_t_list:
        resulting_t += ch
    
    return resulting_s == resulting_t

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
