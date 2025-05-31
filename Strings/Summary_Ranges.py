# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:49:59 2025

@author: jwang
"""

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0:
        return []

    ranges = []
    theRange = str(nums[0])

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
            if theRange == str(nums[i - 1]):
                ranges.append(theRange)
            else:
                theRange = theRange + "->" + str(nums[i - 1])
                ranges.append(theRange)
            theRange = str(nums[i])
        else:
            if i == len(nums) - 1:
                theRange = theRange + "->" + str(nums[i])
    ranges.append(theRange)
    return ranges

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))

nums1 = [0,2,3,4,6,8,9]
print(summaryRanges(nums1))

nums2 = [0,2,3,4,6,8,9,11,13,17,18,19,20,21]
print(summaryRanges(nums2))