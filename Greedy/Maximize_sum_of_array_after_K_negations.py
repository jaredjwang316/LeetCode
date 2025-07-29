# -*- coding: utf-8 -*-
"""
Problem Description:
    Given an integer array nums and an integer k, modify the array in the following way:
        - choose an index i and replace nums[i] with -nums[i].
    You should apply this process exactly k times. You may choose the same index i multiple times.
    Return the largest possible sum of the array after modifying it in this way.

Constraints:
    1 <= nums.length <= 10^4
    -100 <= nums[i] <= 100
    1 <= k <= 10^4
"""

def largestSumAfterKNegations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    for n in range(len(nums)):
        #flip the sign of all negative integers
        if nums[n] < 0 and k > 0:
            nums[n] = nums[n] * -1
            k -= 1
        elif nums[n] == 0:  #we can flip the sign of 0 infinite rimes and still get 0
            return sum(nums)
    
    #sort nums array again so that we can flip the sign of the smallest positive integer if needed
    nums.sort()
    if k > 0 and k % 2 == 1:    
        nums[0] = nums[0] * -1
    
    return sum(nums)

nums = [4,2,3]
k = 1
print(largestSumAfterKNegations(nums, k))   #5 -> Choose index 1 and nums becomes [4,-2,3].

nums2 = [3,-1,0,2]
k2 = 3
print(largestSumAfterKNegations(nums2, k2)) #6 -> Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

nums3 = [2,-3,-1,5,-4]
k3 = 2
print(largestSumAfterKNegations(nums3, k3)) #13 -> Choose indices (1, 4) and nums becomes [2,3,-1,5,4].