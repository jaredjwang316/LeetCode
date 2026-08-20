"""
Problem Description:
    - You are given an integer array nums of length n.
    - A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty 
    subarrays such that:
        * Left subarray contains indices [0, i].
        * Right subarray contains indices [i + 1, n - 1].
    - Return the number of partitions where the difference between the sum of the left and right subarrays 
    is even.

Constraints:
    - 2 <= n == nums.length <= 100
    - 1 <= nums[i] <= 100
"""

def countPartitions(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_sum = sum(nums)

    count_partitions = 0
    left_sum = 0
    for index in range(len(nums) - 1):
        left_sum = left_sum + nums[index]

        if left_sum % 2 == 0 and (total_sum - left_sum) % 2 == 0:     #Case 1: left subarray sum and right subarray sum are both even
            count_partitions += 1
        elif left_sum % 2 == 1 and (total_sum - left_sum) % 2 == 1:   #case 2: left subarray sum and right subarray sum are both odd
            count_partitions += 1
        
    return count_partitions

nums = [10,10,3,7,6]
print(countPartitions(nums))  # Output: 4

nums2 = [1,2,2]
print(countPartitions(nums2))  # Output: 0

nums3 = [2,4,6,8]
print(countPartitions(nums3))  # Output: 3