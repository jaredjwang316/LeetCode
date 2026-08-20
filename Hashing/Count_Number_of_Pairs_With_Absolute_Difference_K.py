"""
Problem Description:
    - Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such 
    that |nums[i] - nums[j]| == k.
    - The value of |x| is defined as:
        * x if x >= 0.
        * -x if x < 0.

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100
    - 1 <= k <= 99
"""

from collections import Counter

def countKDifference(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    num_freq = Counter(nums)

    count_pairs = 0

    for num in num_freq.keys():
        if num + k in num_freq:
            count_pairs = count_pairs + num_freq[num] * num_freq[num + k]
    
    return count_pairs

nums = [1,2,2,1]
k = 1
print(countKDifference(nums, k))  # Output: 4

nums2 = [1,3]
k2 = 3
print(countKDifference(nums2, k2))  # Output: 0

nums3 = [3,2,1,5,4]
k3 = 2
print(countKDifference(nums3, k3))  # Output: 3