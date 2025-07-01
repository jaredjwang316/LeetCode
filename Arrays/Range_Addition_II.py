# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 21:48:39 2025

@author: jwang

Problem Description:
    You are given an m x n matrix M initialized with all 0's and an array of 
    operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented
    by one for all 0 <= x < ai and 0 <= y < bi.

    Count and return the number of maximum integers in the matrix after 
    all the operations.
    
Constraints:
    1 <= m, n <= 4 * 10^4
    0 <= ops.length <= 10^4
    ops[i].length == 2
    1 <= ai <= m
    1 <= bi <= n
"""

def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    if len(ops) == 0:
        return m * n
    
    min_rows = ops[0][0]
    min_col = ops[0][1]

    for i in range(1, len(ops)):
        if ops[i][0] < min_rows:
            min_rows = ops[i][0]
        
        if ops[i][1] < min_col:
            min_col = ops[i][1]
    return min_rows * min_col

m = 3
n = 3
ops = [[2,2],[3,3]]
print(maxCount(m, n, ops))

m2 = 3
n2 = 3
ops2 = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(maxCount(m2, n2, ops2))

m3 = 3
n3 = 3
ops3 = []
print(maxCount(m3, n3, ops3))