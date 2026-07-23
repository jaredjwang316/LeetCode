"""
Problem Description:
    - You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A 
    triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
        * i < j < k,
        * nums[j] - nums[i] == diff, and
        * nums[k] - nums[j] == diff.
    - Return the number of unique arithmetic triplets.

Constraints:
    - 3 <= nums.length <= 200
    - 0 <= nums[i] <= 200
    - 1 <= diff <= 50
    - nums is strictly increasing.
"""

def arithmeticTriplets(nums, diff):
    """
    :type nums: List[int]
    :type diff: int
    :rtype: int
    """
    count_arithmetic_triplets = 0
    unique_nums = set(nums)

    for num in nums:
        if num + diff in unique_nums and num + 2 * diff in unique_nums:
            count_arithmetic_triplets += 1
    
    return count_arithmetic_triplets

nums = [0,1,4,6,7,10]
diff = 3
print(arithmeticTriplets(nums, diff))  # Output: 2

nums2 = [4,5,6,7,8,9]
diff2 = 2
print(arithmeticTriplets(nums2, diff2))  # Output: 2

