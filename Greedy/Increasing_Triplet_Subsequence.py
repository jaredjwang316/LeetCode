# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:33:41 2026

@author: jwang

Problem Description:
    Given an integer array nums, return true if there exists a triple of indices 
    (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such 
    indices exists, return false.

Constraints:
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""

def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    temp1 = pow(2, 31) - 1
    temp2 = pow(2, 31) - 1

    for num in nums:
        if num <= temp1:
            temp1 = num
        elif num <= temp2:
            temp2 = num
        else:
            return True
    return False

nums = [1,2,3,4,5]
print(increasingTriplet(nums))  #True

nums2 = [5,4,3,2,1]
print(increasingTriplet(nums2))  #False

nums3 = [2,1,5,0,4,6]
print(increasingTriplet(nums3))  #True
