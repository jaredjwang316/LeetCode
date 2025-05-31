# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:20:47 2025

@author: jwang
"""

def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    i = 0
    while( i * (i + 1) // 2 < n):
        i += 1
    
    if (i * (i + 1) // 2 ) == n:    #if that row is complete, filled up entirely
        return i
    
    return i - 1

print(arrangeCoins(5))
print(arrangeCoins(8))
print(arrangeCoins(15))