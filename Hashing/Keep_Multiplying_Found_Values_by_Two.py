"""
Problem Description:
    - You are given an array of integers nums. You are also given an integer original which is the 
    first number that needs to be searched for in nums.
    - You then do the following steps:
        * If original is found in nums, multiply it by two (i.e., set original = 2 * 
        original). Otherwise, stop the process.
        * Repeat this process with the new number as long as you keep finding the number.
    - Return the final value of original.

Constraints:
    - 1 <= nums.length <= 1000
    - 1 <= nums[i], original <= 1000
"""

def findFinalValue(nums, original):
    """
    :type nums: List[int]
    :type original: int
    :rtype: int
    """
    unique_nums = set()
    for num in nums:
        if num not in unique_nums:
            unique_nums.add(num)
    
    while(True):
        if original not in unique_nums:
            break
        original = original * 2
    
    return original

nums = [5,3,6,1,12]
original = 3
print(findFinalValue(nums, original))   #Output: 24

nums2 = [2,7,9]
original2 = 4
print(findFinalValue(nums2, original2)) #Output: 4