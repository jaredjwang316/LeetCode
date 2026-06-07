"""
Problem Description:
    - Given an binary array nums and an integer k, return true if all 1's are at least k 
    places away from each other, otherwise return false.

Constraints:
    - 1 <= nums.length <= 10^5
    - 0 <= k <= nums.length
    - nums[i] is 0 or 1
"""

def kLengthApart(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    one_index = -1

    for i in range(len(nums)):
        if nums[i] == 1:
            if one_index != -1 and i - one_index - 1 < k:
                return False
            one_index = i
    return True

nums = [1,0,0,0,1,0,0,1]
k = 2
print(kLengthApart(nums, k)) # Output: true

nums2 = [1,0,0,1,0,1]
k2 = 2
print(kLengthApart(nums2, k2)) # Output: false