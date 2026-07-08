"""
Problem Description:
    - You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
        1. Sort the values at odd indices of nums in non-increasing order.
            * For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values 
            at odd indices 1 and 3 are sorted in non-increasing order.
        2. Sort the values at even indices of nums in non-decreasing order.
            * For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values 
            at even indices 0 and 2 are sorted in non-decreasing order.
    - Return the array formed after rearranging the values of nums.

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
"""

def sortEvenOdd(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    odd_indices = []
    even_indices = []

    for i in range(len(nums)):
        if i % 2 == 0:
            even_indices.append(nums[i])
        else:
            odd_indices.append(nums[i])
    
    odd_indices.sort()  
    even_indices.sort(reverse = True)

    result = []
    for i in range(len(odd_indices) + len(even_indices)):
        result.append(0)
    
    for i in range(len(result)):
        if i % 2 == 1:
            result[i] = odd_indices.pop()   #popping results in non-increasing order
        else:
            result[i] = even_indices.pop()  #popping results in non-decreasing approach
    
    return result

nums = [4,1,2,3]
print(sortEvenOdd(nums))  # Output: [2,3,4,1]

nums2 = [2,1]
print(sortEvenOdd(nums2))  # Output: [2,1]