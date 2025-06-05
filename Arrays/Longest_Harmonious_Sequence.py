# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 21:52:30 2025

@author: jwang
"""

def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_dict = dict()
    for n in nums:
        if n not in num_dict:
            num_dict[n] = 1
        else:
            num_dict[n] += 1
    
    max_hrm_ssq = 0

    for k in num_dict:
        if k + 1 in num_dict:
            lhs = num_dict[k] + num_dict[k + 1]
            max_hrm_ssq = max(max_hrm_ssq, lhs)
    
    return max_hrm_ssq

nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))

nums2 = [1,2,3,4]
print(findLHS(nums2))

nums3 = [1,1,1,1]
print(findLHS(nums3))