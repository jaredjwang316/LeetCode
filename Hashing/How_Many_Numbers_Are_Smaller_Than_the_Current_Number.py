"""
Problem Description:
    - Given the array nums, for each nums[i] find out how many numbers in the array are smaller 
    than it. That is, for each nums[i] you have to count the number of valid j's such that j != i 
    and nums[j] < nums[i].  Return the answer in an array.

Constraints:
    - 2 <= nums.length <= 500
    - 0 <= nums[i] <= 100
"""

def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sorted_nums = []
    for num in nums:
        sorted_nums.append(num)
    sorted_nums.sort()
    
    rank_pos = dict()

    for i, num in enumerate(sorted_nums):
        if num not in rank_pos:
            rank_pos[num] = i
    
    result = []
    for num in nums:
        result.append(rank_pos[num])
    
    return result

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))  # Output: [4,0,1,1,3]

nums2 = [6,5,4,8]
print(smallerNumbersThanCurrent(nums2))  # Output: [2,1,0,3]

nums3 = [7,7,7,7]
print(smallerNumbersThanCurrent(nums3))  # Output: [0,0,0,0]