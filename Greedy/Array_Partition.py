"""
Problem Description:
    Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
    such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Constraints:
    - 1 <= n <= 104
    - nums.length == 2 * n
    - -10^4 <= nums[i] <= 10^4
"""

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    maximized_sum = 0
    for i in range(0, len(nums), 2):
        maximized_sum += min(nums[i], nums[i + 1])
    
    return maximized_sum

nums = [1,4,3,2]
print(arrayPairSum(nums))   #Output: 4

nums2 = [6,2,6,5,1,2]
print(arrayPairSum(nums2))   #Output: 9

