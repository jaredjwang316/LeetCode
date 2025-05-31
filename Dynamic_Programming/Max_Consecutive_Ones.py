# -*- coding: utf-8 -*-
"""
Created on Sat May 31 15:32:43 2025

@author: jwang
"""

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_cc_ones = 0
    count_cc_ones = 0
    for n in nums:
        if n == 0:
            max_cc_ones = max(max_cc_ones, count_cc_ones)
            count_cc_ones = 0   #reset since that breaks the consecutiveness of 1's
        else:
            count_cc_ones += 1
    max_cc_ones = max(max_cc_ones, count_cc_ones)
    return max_cc_ones

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))

nums2 = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums2))