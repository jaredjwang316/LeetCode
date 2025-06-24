# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 14:06:28 2025

@author: jwang

Problem Description:
    Given an integer array nums, move all 0's to the end of it while maintaining 
    the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    count_iterations = 0
    while(count_iterations < len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
        else:
            i = i + 1
        count_iterations += 1

nums = [0,1,0,3,12]
print("nums before moving zeroes:", nums)
moveZeroes(nums)
print("nums after moving zeroes:", nums)

nums2 = [0]
print("nums2 before moving zeroes:", nums2)
moveZeroes(nums2)
print("nums2 after moving zeroes:", nums2)