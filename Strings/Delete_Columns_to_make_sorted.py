# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 10:40:22 2025

@author: jwang

Problem Description:
    You are given an array of n strings strs, all of the same length.
    The strings can be arranged such that there is one on each line, making a grid.
    You want to delete the columns that are not sorted lexicographically. 
    Return the number of columns that you will delete.

Important Constraints:
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] consists of lowercase English letters.

"""

def minDeletionSize(strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    
    if len(strs) == 1:
        return 0
    
    count_delete_col = 0
    for ch in range(len(strs[0])):
        for i in range(1, len(strs), 1):
            if (strs[i])[ch] < (strs[i - 1])[ch]:   #if the column is not lexicographically sorted
                count_delete_col += 1
                break
    
    return count_delete_col

strs = ["cba","daf","ghi"]
print(minDeletionSize(strs))

strs2 = ["a","b"]
print(minDeletionSize(strs2))

strs3 = ["zyx","wvu","tsr"]
print(minDeletionSize(strs3))