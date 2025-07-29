# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 15:34:04 2025

@author: jwang

Problem Description:
    Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

    For example:
    
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].  
"""

def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    columnTitleDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
    'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

    columnNumber = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        columnNumber += columnTitleDict[columnTitle[i]] * pow(26, len(columnTitle) - 1 - i)
    return columnNumber

columnTitle = "A"
print(titleToNumber(columnTitle))   #1

columnTitle2 = "AB"
print(titleToNumber(columnTitle2))   #28

columnTitle3 = "ZY"
print(titleToNumber(columnTitle3))  #701