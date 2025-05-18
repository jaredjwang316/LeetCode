# -*- coding: utf-8 -*-
"""
Created on Sun May 18 10:34:09 2025

@author: jwang
"""

def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    theStack = []
    totalSum = 0
    for ch in operations:
        if ch.lstrip('-').isdigit():
            theStack.append(int(ch))    #record the new score
        elif ch == '+':
            theStack.append(theStack[len(theStack) - 2] + theStack[len(theStack) - 1] )
        elif ch == 'C':
            theStack.pop()  #invalidate the previous score
        elif ch == 'D':
            prevScore = theStack[len(theStack) - 1]
            theStack.append(2*prevScore)
    
    for val in theStack:
        totalSum += val
    return totalSum

ops = ["5","2","C","D","+"]
print(calPoints(ops))

ops1 = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops1))

ops2 = ["1", "C"]
print(calPoints(ops2))
