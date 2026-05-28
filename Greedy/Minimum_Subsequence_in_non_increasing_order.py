"""
Problem Description:
    - Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater 
    than the sum of the non included elements in such subsequence. 
    - If there are multiple solutions, return the subsequence with minimum size and if there still 
    exist multiple solutions, return the subsequence with the maximum total sum of all its elements. 
    A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
    - Note that the solution with the given constraints is guaranteed to be unique. Also return 
    the answer sorted in non-increasing order.

Constraints:
    - 1 <= nums.length <= 500
    - 1 <= nums[i] <= 100
"""

def minSubsequence(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    total_sum = sum(nums)
    nums.sort()
    subsum = 0
    result = []
    for i in range(len(nums) - 1, -1, -1):
        if 2 * subsum <= total_sum:
            result.append(nums[i])
            subsum += nums[i]
    
    return result

nums = [4,3,10,9,8]
print(minSubsequence(nums)) # [10,9]

nums2 = [4,4,7,6,7]
print(minSubsequence(nums2)) # [7,7,6]