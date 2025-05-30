# -*- coding: utf-8 -*-
"""
Created on Fri May 30 17:17:06 2025

@author: jwang
"""

def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    #note robot starts at the origin
    horizontal = 0
    vertical = 0

    for i in range(len(moves)):
        if moves[i] == 'U':
            vertical += 1
        elif moves[i] == 'D':   #down is in the opposite of up
            vertical -= 1
        elif moves[i] == 'L':   #left is in the opposite of right
            horizontal -= 1
        else:   #if moves[i] == 'R'
            horizontal += 1

    if vertical == 0 and horizontal == 0:
        return True
    return False

moves = "UD"
print(judgeCircle(moves))

moves1 = "LL"
print(judgeCircle(moves1))