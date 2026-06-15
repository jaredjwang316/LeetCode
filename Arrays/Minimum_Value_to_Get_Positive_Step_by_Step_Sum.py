"""
Problem Description:
    - Given an array of integers nums, you start with an initial positive value startValue.  In each 
    iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
    - Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Constraints:
    - 1 <= nums.length <= 100
    - -100 <= nums[i] <= 100
"""

def minStartValue(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prefix_sum = 0
    minSum = 0

    for num in nums:
        prefix_sum += num
        minSum = min(minSum, prefix_sum)

    return 1 - minSum

nums = [-3,2,-3,4,2]
print(minStartValue(nums))    #5

nums2 = [1,2]
print(minStartValue(nums2))   #1 because the minimum start value should be positive

nums3 = [1,-2,-3]
print(minStartValue(nums3))   #5