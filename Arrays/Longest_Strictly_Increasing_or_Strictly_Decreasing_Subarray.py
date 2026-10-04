"""
Problem Description:
    - You are given an array of integers nums.  Return the length of the longest subarray 
    of nums which is either strictly increasing or strictly decreasing.

Constraints:
    - 1 <= nums.length <= 50
    - 1 <= nums[i] <= 50
"""

def longestMonotonicSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """       
    answer = -1

    strictly_increase = 1
    strictly_decrease = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            strictly_increase += 1
            strictly_decrease = 1
            answer = max(answer, strictly_increase)
        elif nums[i] == nums[i - 1]:
            # the current number could the start of a strictly decreasing or strictly increasing subarray
            strictly_increase = 1   
            strictly_decrease = 1
        else:
            strictly_decrease += 1
            strictly_increase = 1
            answer = max(answer, strictly_decrease)
    
    if answer == -1:
        return 1

    return answer

nums = [1,4,3,3,2]
print(longestMonotonicSubarray(nums))   #2

nums2 = [3,3,3,3]
print(longestMonotonicSubarray(nums2))  #1

nums3 = [3,2,1]
print(longestMonotonicSubarray(nums3))  #3

