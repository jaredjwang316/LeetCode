# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 15:59:37 2025

@author: jwang
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    target_indicies = []
    num_index = dict()
    for i in range(len(nums)):
        if nums[i] not in num_index:
            num_index[nums[i]] = i
        if target - nums[i] in num_index and num_index[target - nums[i]] != i:
            target_indicies.append(num_index[target - nums[i]] )
            target_indicies.append(i)
            break
    
    return target_indicies

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

nums2 = [3,2,4]
target2 = 6
print(twoSum(nums2, target2))

nums3 = [3,3] 
target3 = 6
print(twoSum(nums3, target3))