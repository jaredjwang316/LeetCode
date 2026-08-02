"""
Problem Description:
    - You are given a 0-indexed array nums of integers.
    - A triplet of indices (i, j, k) is a mountain if:
        * i < j < k
        * nums[i] < nums[j] and nums[k] < nums[j]
    - Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

Constraints:
    - 3 <= nums.length <= 50
    - 1 <= nums[i] <= 50
"""

def minimumSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    leftMin = []
    rightMin = []

    for i in range(len(nums)):
        leftMin.append(0)
        rightMin.append(0)
    
    leftMin[0] = nums[0]    #keep track of the minimum value that we have visited so far when traversing from left to right of nums
    rightMin[-1] = nums[-1] #keep track of the minimum value that we have visited so far when traversing from right to left of nums

    for i in range(1, len(leftMin)):
        leftMin[i] = min(nums[i], leftMin[i - 1])
    
    for i in range(len(rightMin) - 2, -1, -1):
        rightMin[i] = min(nums[i], rightMin[i + 1])

    minTripletSum = float('inf')

    for i in range(1, len(nums) - 1, 1):
        if leftMin[i - 1] < nums[i] and nums[i] > rightMin[i + 1]:
            minTripletSum = min(minTripletSum, leftMin[i - 1] + nums[i] + rightMin[i + 1])

    if minTripletSum == float('inf'):   #if no such mountain triplet exists
        return -1
    return minTripletSum

nums = [8,6,1,5,3]
print(minimumSum(nums))  # Output: 9

nums2 = [5,4,8,7,10,2]
print(minimumSum(nums2))  # Output: 13

nums3 = [6,5,4,3,4,5]
print(minimumSum(nums3))  # Output: -1

nums4 = [1,2,3,4,5]
print(minimumSum(nums4))  # Output: -1