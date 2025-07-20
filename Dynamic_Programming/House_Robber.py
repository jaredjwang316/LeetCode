# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 10:10:56 2025

@author: jwang

Problem Description:
    You are a professional robber planning to rob houses along a street. Each 
    house has a certain amount of money stashed, the only constraint stopping 
    you from robbing each of them is that adjacent houses have security systems 
    connected and it will automatically contact the police if two adjacent 
    houses were broken into on the same night.
    
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    
    dp = []
    for i in range(len(nums)):
        dp.append(0)
    
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(dp)):
        #either he robs house i - 1 house thus cannot rob the ith house
        #or he robs the ith house and accumulates the money he obtained from robbing i - 2 house and before
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) 
    
    return dp[len(nums) - 1]

nums = [1,2,3,1]
print(rob(nums))    #4

nums2 = [2,7,9,3,1]
print(rob(nums2))   #12

nums3 = [2,1,1,2]
print(rob(nums3))   #4

nums4 = [3,1,2,5]
print(rob(nums4))   #8
