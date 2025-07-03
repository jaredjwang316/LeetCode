# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 22:12:48 2025

@author: jwang

Problem Description:
    Given an array nums of n integers, return an array of all the unique 
    quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target

    You may return the answer in any order.

Constraints:
    1 <= nums.length <= 200
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
"""

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return []
        
    quadruplets = []
    nums.sort()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            k = j + 1
            l = len(nums) - 1
            while(k < l):
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    if [nums[i], nums[j], nums[k], nums[l]] not in quadruplets:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                else:
                    l -= 1
    
    return quadruplets

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))

nums2 = [2,2,2,2,2]
target2 = 8
print(fourSum(nums2, target2))