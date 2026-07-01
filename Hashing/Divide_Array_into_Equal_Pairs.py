"""
Problem Description:
    - You are given an integer array nums consisting of 2 * n integers.
    - You need to divide nums into n pairs such that:
        * Each element belongs to exactly one pair.
        * The elements present in a pair are equal.
    - Return true if nums can be divided into n pairs, otherwise return false.

Constraints:
    - nums.length == 2 * n
    - 1 <= n <= 500
    - 1 <= nums[i] <= 500
"""

from collections import Counter

def divideArray(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    formable_pairs = 0

    num_freq = Counter(nums)
    for v in num_freq.values():
        if v % 2 == 0:
            formable_pairs += (v // 2)  #we can form v // 2 pairs of that element such that each element present in that pair are equal
    
    if formable_pairs == (len(nums) // 2):
        return True
    return False

nums = [3,2,3,2,2,2]
print(divideArray(nums))  # Output: True

nums2 = [1,2,3,4]
print(divideArray(nums2))  # Output: False

