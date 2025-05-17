# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:29:16 2025

@author: jwang
"""

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    pascal = [[1], [1,1]]

    #edge cases
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
        
    pascal.append([1, 1])
    for i in range(2, 34):
        new_list = [1]
        for j in range(len(pascal[len(pascal) - 1]) - 1) :
            new_list.append( (pascal[len(pascal) - 1])[j] +  (pascal[len(pascal) - 1])[j + 1])
        new_list.append(1)
        pascal.append(new_list)  

    return pascal[rowIndex + 1]      

print(getRow(1))
print(getRow(5))
print(getRow(6))

