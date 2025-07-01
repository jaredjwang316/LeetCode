# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:17:46 2025

@author: jwang

Problem Description:
    Given an integer array nums, return the largest perimeter of a triangle 
    with a non-zero area, formed from three of these lengths. If it is impossible 
    to form any triangle of a non-zero area, return 0.
    
Constraints:
    
    3 <= nums.length <= 10^4
    1 <= nums[i] <= 10^6

"""

def isValidTriangle(s1, s2, s3):
    if s3 >= (s1 + s2):
        return False
    return True
def largestPerimeter(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    largest_perimeter = 0

    nums.sort()

    for i in range(len(nums) - 1, 1, -1):
        if isValidTriangle(nums[i - 2], nums[i - 1], nums[i]):
            largest_perimeter = max(largest_perimeter, nums[i - 2] + nums[i - 1] + nums[i])
    
    return largest_perimeter

nums = [2,1,2]
print(largestPerimeter(nums))

nums2 = [1,2,1,10]
print(largestPerimeter(nums2))