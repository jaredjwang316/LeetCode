# -*- coding: utf-8 -*-
"""
Created on Sat May 31 09:48:41 2025

@author: jwang
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1

    while(high >= 0):
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        if nums[low] > target:
            return low
        
        low += 1
        high -= 1
        
        
    return len(nums)

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

target2 = 2
print(searchInsert(nums, target2))

target3 = 7
print(searchInsert(nums, target3))

nums1= [1, 3]
target4 = 2
print(searchInsert(nums1, target4))

nums2 = [1, 3, 5]
target5 = 4 
print(searchInsert(nums2, target5))

nums3 = [3]
target6 = 5
print(searchInsert(nums3, target6))


