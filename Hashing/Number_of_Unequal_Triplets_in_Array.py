"""
Problem Description:
    - You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) 
    that meet the following conditions:
        * 0 <= i < j < k < nums.length
        * nums[i], nums[j], and nums[k] are pairwise distinct.
            - In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
    - Return the number of triplets that meet the conditions.

Constraints:
    - 3 <= nums.length <= 100
    - 1 <= nums[i] <= 1000
"""

from collections import Counter

def unequalTriplets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_freq = Counter(nums)

    left = 0    #processed groups
    right = len(nums)   #unprocessed groups

    unequal_triplets = 0
    for v in num_freq.values():
        right -= v  #this group is currently being processed, thus not considered unprocessed
        unequal_triplets = unequal_triplets + left * v * right
        left += v   #this group is already processed
    
    return unequal_triplets

nums = [4,4,2,4,3]
print(unequalTriplets(nums))    #Expected output: 3

nums2 = [1,1,1,1,1]
print(unequalTriplets(nums2))    #Expected output: 0

