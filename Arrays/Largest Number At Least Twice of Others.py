# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 14:17:52 2025

@author: jwang
"""

"""
Problem Description:
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as 
    much as every other number in the array. If it is, return the index of 
    the largest element, or return -1 otherwise.

Important Constraints:
    2 <= nums.length <= 50
    0 <= nums[i] <= 100
    The largest element in nums is unique.
"""

def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    largest_index = 0
    max_val = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            largest_index = i
    
    second_max_val = 0
    for i in range(len(nums)):
        if nums[i] > second_max_val and i != largest_index:
            second_max_val = nums[i]
    
    if max_val >= 2 * second_max_val:
        return largest_index
    return -1

nums = [3,6,1,0]
print(dominantIndex(nums))

nums2 = [1, 2, 3, 4]
print(dominantIndex(nums2))

nums3 = [1, 0]
print(dominantIndex(nums3))

nums4 = [2, 0, 0, 3]
print(dominantIndex(nums4))

