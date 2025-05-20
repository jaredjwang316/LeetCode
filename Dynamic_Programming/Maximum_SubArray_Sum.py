# -*- coding: utf-8 -*-
"""
Created on Tue May 20 18:01:21 2025

@author: jwang
"""

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = 0
    dp = []
    for n in range(len(nums)):
        if n == 0:
            dp.append(nums[n])
        else:
            dp.append(max(nums[n], dp[n - 1] + nums[n]))
    
    max_index = -1
    max_sum = dp[0]

    for d in dp:
        if d > max_sum:
            max_sum = d

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

nums2 = [1]
print(maxSubArray(nums2))

nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums3))