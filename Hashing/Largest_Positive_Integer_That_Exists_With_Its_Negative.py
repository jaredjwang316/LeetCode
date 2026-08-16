"""
Problem Description:
    - Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists 
    in the array.
    - Return the positive integer k. If there is no such integer, return -1.

Constraints:
    - 1 <= nums.length <= 1000
    - -1000 <= nums[i] <= 1000
    - nums[i] != 0
"""

def findMaxK(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique_nums = set(nums)

    largest = -1
    for num in nums:
        if num > 0 and (-1) * num in unique_nums:
            largest = max(largest, num)
    
    return largest

nums = [-1,2,-3,3]
print(findMaxK(nums))  # Output: 3

nums2 = [-1,10,6,7,-7,1]
print(findMaxK(nums2))  # Output: 7

nums3 = [-10,8,6,7,-2,-3]
print(findMaxK(nums3))  # Output: -1