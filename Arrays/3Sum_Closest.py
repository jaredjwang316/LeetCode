# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 15:16:55 2025

@author: jwang

Problem Description:
    Given an integer array nums of length n and an integer target, find three 
    integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4
"""


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while(j < k):
            if nums[i] + nums[j] + nums[k] == target:
                return target
            elif nums[i] + nums[j] + nums[k] < target:
                if abs(target - (nums[i] + nums[j] + nums[k])) < abs(target - closest):
                    closest = nums[i] + nums[j] + nums[k]
                j += 1
            else:
                if abs(target - (nums[i] + nums[j] + nums[k])) < abs(target - closest):
                    closest = nums[i] + nums[j] + nums[k]
                k -= 1

    return closest                             
    
nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))    #2 -> (-1 + 2 + 1 = 2).

nums2 = [0,0,0]
target2 = 1
print(threeSumClosest(nums2, target2))  #0 -> 0 + 0 + 0 = 0

nums3 = [4,0,5,-5,3,3,0,-4,-5]
target3 = -2
print(threeSumClosest(nums3, target3))  #-2