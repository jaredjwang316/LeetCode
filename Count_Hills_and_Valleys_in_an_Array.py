# -*- coding: utf-8 -*-
"""
Created on Mon May 26 14:29:11 2025

@author: jwang
"""

def countHillValley(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    count_hills_or_valleys = 0
    isHill = True
    isValley = True
    for i in range(1, len(nums) - 1):
        isHill = True
        isValley = True
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[i]:
                isHill = False
                isValley = True
                break
            elif nums[j] < nums[i]:
                isValley = False
                isHill = True
                break
            else:
                isHill = False
                isValley = False                    
        
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                isHill = False
                break
            elif nums[j] < nums[i]:
                isValley = False
                break
            else:
                isHill = False
                isValley = False    

        if isHill or isValley:
            count_hills_or_valleys += 1
    
    return count_hills_or_valleys

nums = [2,4,1,1,6,5]
print(countHillValley(nums))

nums2 = [6,6,5,5,4,1]
print(countHillValley(nums2))

nums3 = [2,4,1,6,5]
print(countHillValley(nums3))