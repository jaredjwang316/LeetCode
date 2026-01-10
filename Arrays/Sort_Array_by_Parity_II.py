"""
Problem Description:
    - Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
    - Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
    - Return any answer array that satisfies this condition.

Constraints:
    - 2 <= nums.length <= 2 * 10^4
    - nums.length is even.
    - Half of the integers in nums are even.
    - 0 <= nums[i] <= 1000
"""

def sortArrayByParityII(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 0
    j = 1
    while(i < len(nums) and j < len(nums)):
        if nums[i] % 2 == 0:    #satisfy that even indices contain even number
            i += 2
        elif nums[j] % 2 == 1:  #satisfy that odd indices contain odd number  
            j += 2
        else:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 2
            j += 2
    return nums

nums = [4,2,5,7]
print(sortArrayByParityII(nums))  #Output: [4,5,2,7] or any other valid arrangement

nums2 = [2,3]
print(sortArrayByParityII(nums2))  #Output: [2,3]

nums3 = [2,3,1,1,4,0,0,4,3,3]
print(sortArrayByParityII(nums3))  #Output: [2,3,0,1,4,1,0,3,4,3]