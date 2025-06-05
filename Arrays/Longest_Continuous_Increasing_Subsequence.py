# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 13:51:22 2025

@author: jwang

Problem Description:
    Given an unsorted array of integers nums, return the length of the longest 
    continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r (l < r) 
    such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for 
    each l <= i < r, nums[i] < nums[i + 1].
"""

def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest_CIS = 1
    cc = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cc += 1
        else:
            longest_CIS = max(longest_CIS, cc)
            cc = 1
    longest_CIS = max(longest_CIS, cc)
    return longest_CIS

nums = [1,3,5,4,7]
print(findLengthOfLCIS(nums))

nums1 = [2,2,2,2,2]
print(findLengthOfLCIS(nums1))

nums2 = [1,3,5,7]
print(findLengthOfLCIS(nums2))