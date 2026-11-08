"""
Problem Description:
    - You are given a 0-indexed array nums of length n containing distinct positive integers. Return the 
    minimum number of right shifts required to sort nums and -1 if this is not possible.
    - A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
    - nums contains distinct integers.
"""

def minimumRightShifts(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    count = 0
    pos_index = 0
    for i in range(len(nums)):
        if nums[i] > nums[ (i + 1) % len(nums)]:
            count += 1
            pos_index = i
    
    if count == 0:  #the list is already sorted
        return 0
    elif count == 1:
        return len(nums) - (pos_index + 1)

    return -1 

nums = [3,4,5,1,2]
print(minimumRightShifts(nums))     #Output: 2

nums2 = [1,3,5]
print(minimumRightShifts(nums2))    #Output: 0

nums3 = [2,1,4]
print(minimumRightShifts(nums3))    #Output: -1