# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 17:55:13 2025

@author: jwang

You are given an array of strings tokens that represents an arithmetic expression 
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """

    theStack = []

    for t in tokens:
        if t.isdigit() == True or (t[0] == '-' and t[1:].isdigit() == True):
            theStack.append(t)
        elif t == '+':
            intermediate1 = theStack.pop()
            intermediate2 = theStack.pop()
            theStack.append(int(intermediate1) + int(intermediate2))
        elif t == '-':
            intermediate1 = theStack.pop()
            intermediate2 = theStack.pop()
            theStack.append(int(intermediate2) - int(intermediate1))  
        elif t == '*':
            intermediate1 = theStack.pop()
            intermediate2 = theStack.pop()
            theStack.append(int(intermediate1) * int(intermediate2))            
        elif t == '/':
            intermediate1 = theStack.pop()
            intermediate2 = theStack.pop()
            if (int(intermediate2) > 0 and int(intermediate1) < 0) or (int(intermediate2) < 0 and int(intermediate1) > 0):
                theStack.append( (-1) * (abs(int(intermediate2)) // abs(int(intermediate1))) )
            else:
                theStack.append(int(intermediate2) // int(intermediate1)) 
    return int(theStack[-1])

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))  # ((2 + 1) * 3) = 9

tokens2 = ["4","13","5","/","+"]
print(evalRPN(tokens2)) # (4 + (13 / 5)) = 6

tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens3)) # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22 

tokens4 = ["-200", "9", "/"]
print(evalRPN(tokens4)) #-22
