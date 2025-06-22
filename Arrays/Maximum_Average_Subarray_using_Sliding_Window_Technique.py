# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 18:36:51 2025

@author: jwang

Problem Description:
    - You are given an integer array nums consisting of n elements, and an integer k.
    - Find a contiguous subarray whose length is equal to k that has the maximum 
    average value and return this value. Any answer with a calculation error 
    less than 10-5 will be accepted.

Important Constraints:
    n == nums.length
    1 <= k <= n <= 10^5
    -104 <= nums[i] <= 104

"""

def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    subArray_sum = 0
    for i in range(k):
        subArray_sum += nums[i]
    
    max_sum_with_k_elements = subArray_sum
    for i in range(1, len(nums) - k + 1):
        subArray_sum = subArray_sum + nums[i + k - 1] - nums[i - 1]
        if subArray_sum > max_sum_with_k_elements:
            max_sum_with_k_elements = max(max_sum_with_k_elements, subArray_sum)
    
    return float(max_sum_with_k_elements) / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))  #12.75

nums2 = [5]
k2 = 1
print(findMaxAverage(nums2, k2))    #5.00
