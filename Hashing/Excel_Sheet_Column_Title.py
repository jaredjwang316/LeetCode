# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 15:25:09 2025

@author: jwang

Problem Description:
    Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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
    1 <= columnNumber <= 2^31 - 1
"""

def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    columnDict = {0: 'Z', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M',
    14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y'}

    title = ""
    while (columnNumber > 0):
        flag = False
        title = columnDict[columnNumber % 26] + title
        if columnNumber % 26 == 0:
            flag = True
        columnNumber = columnNumber // 26
        if flag:
            columnNumber -= 1
            
    return title

columnNumber = 1
print(convertToTitle(columnNumber)) #A

columnNumber2 = 28
print(convertToTitle(columnNumber2))    #AB

columnNumber3 = 701
print(convertToTitle(columnNumber3))    #ZY

columnNumber4 = 52
print(convertToTitle(columnNumber4))    #AZ