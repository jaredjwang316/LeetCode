"""
Problem Description:
    - You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array 
    and increment it by 1.
        * For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
    - Return the minimum number of operations needed to make nums strictly increasing.
    - An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array 
    of length 1 is trivially strictly increasing.

Constraints:
    - 1 <= nums.length <= 5000
    - 1 <= nums[i] <= 10^4
"""

def minOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count_operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            count_operations = count_operations + (nums[ i - 1] - nums[i] + 1)
            nums[i] = nums[i - 1] + 1
    
    return count_operations

nums = [1,1,1]
print(minOperations(nums))  # Output: 3

nums2 = [1,5,2,4,1]
print(minOperations(nums2))  # Output: 14

nums3 = [9]
print(minOperations(nums3))  # Output: 0