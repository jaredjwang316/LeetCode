# -*- coding: utf-8 -*-
"""
Created on Sat May 17 22:08:38 2025

@author: jwang
"""

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique_nums = set()

    for n in nums:
        if n not in unique_nums:
            unique_nums.add(n)
        else:
            return n
    
    return -1