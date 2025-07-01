# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 12:30:48 2025

@author: jwang

Problem Description:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

Constraints:
    3 <= nums.length <= 3000
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    triplets = []

    nums.sort()
    for i in range(len(nums) - 2):

        j = i + 1
        k = len(nums) - 1

        while(j < k):
            if nums[i] + nums[j] + nums[k] == 0:
                if [nums[i], nums[j], nums[k]] not in triplets:
                    triplets.append([nums[i], nums[j], nums[k]])
                j += 1

            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

    return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums2 = [0,1,1]
print(threeSum(nums2))

nums3 = [0, 0, 0]
print(threeSum(nums3))