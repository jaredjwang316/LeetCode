# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:34:58 2025

@author: jwang
"""

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    pascal = []
    pascal.append([1])

    if numRows == 1:
        return pascal
    elif numRows == 2:
        return [[1], [1, 1]]
    
    pascal.append([1, 1])
    for i in range(2, numRows):
        new_list = [1]
        for j in range(len(pascal[len(pascal) - 1]) - 1) :
            new_list.append( (pascal[len(pascal) - 1])[j] +  (pascal[len(pascal) - 1])[j + 1])
        new_list.append(1)
        pascal.append(new_list)
    
    return pascal