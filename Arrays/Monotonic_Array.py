# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 14:23:55 2025

@author: jwang
"""

"""
Problem Description:
    An array is monotonic if it is either monotone increasing or monotone decreasing.
    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
    Given an integer array nums, return true if the given array is monotonic, or false otherwise.
    
Constraints:
    1 <= nums.length <= 10^5
    
"""

def isMonotonic(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    monoIncrease = True
    monoDecrease = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            monoDecrease = False
        elif nums[i] < nums[i - 1]:
            monoIncrease = False
    
    if monoIncrease == True or monoDecrease == True:
        return True
    
    return False

nums = [1, 2, 2, 3]
print("Is", nums, "Monotonic?", isMonotonic(nums))

nums2 = [6, 5, 4, 4]
print("Is", nums2, "Monotonic?", isMonotonic(nums2))

nums3 = [1, 3, 2]
print("Is", nums3, "Monotonic?", isMonotonic(nums3))

nums4 = [13]
print("Is", nums4, "Monotonic?", isMonotonic(nums4))