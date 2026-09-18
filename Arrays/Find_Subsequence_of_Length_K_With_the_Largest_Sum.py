"""
Problem Description:
    - You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the 
    largest sum.
    - Return any such subsequence as an integer array of length k.
    - A subsequence is an array that can be derived from another array by deleting some or no elements without changing 
    the order of the remaining elements.

Constraints:
    - 1 <= nums.length <= 1000
    - -10^5 <= nums[i] <= 10^5
    - 1 <= k <= nums.length
"""

def maxSubsequence(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    value_index_pair = []
    for i, num in enumerate(nums):
        value_index_pair.append( (num, i) )
    
    # Sort by the element value in nums in descending order
    value_index_pair = sorted(value_index_pair, key = lambda x: -x[0])
    
    # extract the largest k values in the given list
    extract_largest_k_values = value_index_pair[0:k]

    # Sort by index occurrence in ascending order to prevent changing the order of the remaining elements
    extract_largest_k_values = sorted(extract_largest_k_values, key = lambda x: x[1])

    result = []
    for pair in extract_largest_k_values:
        result.append(pair[0])
        
    return result

nums = [2,1,3,3]
k = 2
print(maxSubsequence(nums, k))  # Output: [3, 3]

nums2 = [-1,-2,3,4]
k2 = 3
print(maxSubsequence(nums2, k2))    # Output: [-1, 3, 4]

nums3 = [3,4,3,3]
k3 = 2
print(maxSubsequence(nums3, k3))    # Output: [3, 4]