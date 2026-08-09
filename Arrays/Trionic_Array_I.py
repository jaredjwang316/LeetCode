"""
Problem Description:
    - You are given an integer array nums of length n.
    - An array is trionic if there exist indices 0 < p < q < n − 1 such that:
        * nums[0...p] is strictly increasing,
        * nums[p...q] is strictly decreasing,
        * nums[q...n − 1] is strictly increasing.
    - Return true if nums is trionic, otherwise return false.

Constraints:
    - 3 <= n <= 100
    - -1000 <= nums[i] <= 1000
"""

def isTrionic(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    index = 0

    #strictly increasing
    while(index < len(nums) - 1 and nums[index] < nums[index + 1]):
        index += 1
    
    if index == 0 or index == len(nums) - 1:
        return False
    
    p = index

    #strictly decreasing
    while(index < len(nums) - 1 and nums[index] > nums[index + 1]):
        index += 1
    
    if index == p or index == len(nums) - 1:
        return False

    #strictly increasing again
    while(index < len(nums) - 1 and nums[index] < nums[index + 1]):
        index += 1
    
    if index != len(nums) - 1:
        return False
    
    return True

nums = [1,3,5,4,2,6]
print(isTrionic(nums))  # Output: True

nums2 = [2,1,3]
print(isTrionic(nums2))  # Output: False