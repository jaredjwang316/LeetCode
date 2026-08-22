"""
Problem Description:
    - You are given an integer array nums.
    - An element nums[i] is considered valid if it satisfies at least one of the following conditions:
        * It is strictly greater than every element to its left.
        * It is strictly greater than every element to its right.
    - The first and last elements are always valid.
    - Return an array of all valid elements in the same order as they appear in nums.

Constraints:
    - 1 <= nums.length <= 100
    - 1 <= nums[i] <= 100
"""

def findValidElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefix_left = []    #used to keep track of the greatest element that we have encountered so far as we traverse the array from left to right
    for i in range(len(nums)):
        prefix_left.append(0)
    prefix_left[0] = nums[0]
    
    for i in range(1, len(prefix_left)):
        prefix_left[i] = max(prefix_left[i - 1], nums[i])

    prefix_right = []   #used to keep track of the greatest element that we have encountered so far as we traverse the array from right to left
    for i in range(len(nums)):
        prefix_right.append(0)
    prefix_right[-1] = nums[-1]
    
    for i in range(len(prefix_right) - 2, -1, -1):
        prefix_right[i] = max(prefix_right[i + 1], nums[i])

    valid_elements = []
    for i in range(len(nums)):
        if i == 0 or nums[i] > prefix_left[i - 1]:    # check if it is the first element or if the current element is strictly greater than every element to its left
            valid_elements.append(nums[i])
        elif i == len(nums) - 1 or nums[i] > prefix_right[i + 1]:    # check if it is the last element or if the current element is strictly greater than every element to its right
            valid_elements.append(nums[i])
    
    return valid_elements

nums = [1,2,4,2,3,2]
print(findValidElements(nums))  # Output: [1,2,4,3,2]

nums2 = [5,5,5,5]
print(findValidElements(nums2))  # Output: [5,5]

nums3 = [1]
print(findValidElements(nums3))  # Output: [1]