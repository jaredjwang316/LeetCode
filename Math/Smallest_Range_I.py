# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 22:29:02 2025

@author: jwang

Problem Description:
    You are given an integer array nums and an integer k.

    In one operation, you can choose any index i where 0 <= i < nums.length and 
    change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. 
    You can apply this operation at most once for each index i.

    The score of nums is the difference between the maximum and minimum elements in nums.
    Return the minimum score of nums after applying the mentioned operation 
    at most once for each index in it.

Constraints:
    
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^4
    0 <= k <= 10^4
"""

def smallestRangeI(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """


    maxVal = nums[0]
    minVal = nums[0]

    for n in nums:
        if n > maxVal:
            maxVal = n
    
    for n in nums:
        if n < minVal:
            minVal = n
    
    if maxVal - minVal - 2 * k >= 0:
        return maxVal - minVal - 2 * k
    
    return 0

nums = [1]
k = 0
print(smallestRangeI(nums, k))

nums2 = [0,10] 
k2 = 2
print(smallestRangeI(nums2, k2))

nums3 = [1,3,6] 
k3 = 3
print(smallestRangeI(nums3, k3))

nums4 = [2,7,2]
k4 = 1
print(smallestRangeI(nums4, k4))