"""
Problem Description:
    - Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray 
    in nums.  A subarray is defined as a contiguous sequence of numbers in an array.

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
"""

def maxAscendingSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    consecutive_increasing_sum = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            consecutive_increasing_sum += nums[i]
        else:
            result = max(result, consecutive_increasing_sum)
            consecutive_increasing_sum = nums[i]
    
    result = max(result, consecutive_increasing_sum)
    return result

nums = [10,20,30,5,10,50]
print(maxAscendingSum(nums))    #Output: 65

nums2 = [10,20,30,40,50]
print(maxAscendingSum(nums2))   #Output: 150

nums3 = [12,17,15,13,10,11,12]
print(maxAscendingSum(nums3))   #Output: 33