"""
Problem Description:
    - You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
    - For every unique integer target in nums, count the number of times target immediately follows an 
    occurrence of key in nums. In other words, count the number of indices i such that:
        * 0 <= i <= nums.length - 2
        * nums[i] == key
        * nums[i + 1] == target
    - Return the target with the maximum count. The test cases will be generated such that the target with 
    maximum count is unique.

Constraints:
    - 2 <= nums.length <= 1000
    - 1 <= nums[i] <= 1000
    - The test cases will be generated such that the answer is unique.
"""

def mostFrequent(nums, key):
    """
    :type nums: List[int]
    :type key: int
    :rtype: int
    """
    count_key_target_pair_occurrences = dict()

    for i in range(len(nums) - 1):
        if nums[i] == key:
            if (nums[i], nums[i + 1]) not in count_key_target_pair_occurrences:
                count_key_target_pair_occurrences[ (nums[i], nums[i + 1]) ] = 1
            else:
                count_key_target_pair_occurrences[ (nums[i], nums[i + 1]) ] += 1
    
    max_target_occurrence = -1

    for val in count_key_target_pair_occurrences.values():
        if val > max_target_occurrence:
            max_target_occurrence = val
    
    for k,v in count_key_target_pair_occurrences.items():
        if v == max_target_occurrence:
            return k[1]
    
    return -1

nums = [1,100,200,1,100]
key = 1
print(mostFrequent(nums, key))  #Output: 100

nums2 = [2,2,2,2,3]
key2 = 2
print(mostFrequent(nums2, key2))    #Output: 2