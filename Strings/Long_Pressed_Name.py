# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 10:59:34 2025

@author: jwang

Problem Description:
    - Your friend is typing his name into a keyboard. Sometimes, when typing a 
    character c, the key might get long pressed, and the character will be typed 1 or more times.

    - You examine the typed characters of the keyboard. Return True if it is possible 
    that it was your friends name, with some characters (possibly none) being long pressed.
"""

def isLongPressedName(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    i = 0
    j = 0
    
    while (i < len(name) and j < len(typed)):
        if name[i] == typed[j]:
            i = i + 1
            j = j + 1
        elif j > 0 and typed[j] == typed[j - 1]:    #if long pressed
            j += 1
        else:
            return False
    
    while (j < len(typed)):
        if typed[j] != typed[j - 1]:
            return False
        j += 1
    return i == len(name) 

name = "alex"
typed = "aaleex"
print(isLongPressedName(name, typed))   #True: 'a' and 'e' in 'alex' were long pressed.

name2 = "saeed"
typed2 = "ssaaedd"
#False: 'e' must have been pressed twice, but it was not in the typed output.
print(isLongPressedName(name2, typed2))   

name3 = "alex"
typed3 = "aaleexa"
print(isLongPressedName(name3, typed3))     #False

name4 = "vtkgn"
typed4 = "vttkgnn"
print(isLongPressedName(name4, typed4))     #True