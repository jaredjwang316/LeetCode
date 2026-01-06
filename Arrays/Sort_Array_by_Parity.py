"""
Problem Description:
    Given an integer array nums, move all the even integers at the beginning of the array followed 
    by all the odd integers.

    Return any array that satisfies this condition.

Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
"""

def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    left = 0
    right = len(nums) - 1
    while(left <= right):
        if nums[left] % 2 == 0:
            left += 1
            continue
        elif nums[right] % 2 == 1:
            right -= 1
            continue 

        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums

nums = [3,1,2,4]
print(sortArrayByParity(nums))  #[4,2,1,3]

nums2 = [0]
print(sortArrayByParity(nums2))  #[0]