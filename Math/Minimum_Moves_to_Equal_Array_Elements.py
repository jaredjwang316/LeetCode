"""
Problem Description:
    - Given an integer array nums of size n, return the minimum number of moves required to make 
    all array elements equal.  
    - In one move, you can increment n - 1 elements of the array by 1.

Constraints:
    - n == nums.length
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - The answer is guaranteed to fit in a 32-bit integer.
"""

def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Idea: if we increase n - 1 elements of the array by 1, we are essentially decreasing 1 of the element in the array by 1
    minNum = min(nums)

    count_min_moves = 0
    for num in nums:
        count_min_moves = count_min_moves + (num - minNum)
    
    return count_min_moves

nums = [1,2,3]
print(minMoves(nums))   #Output: 3

nums2 = [1,1,1]
print(minMoves(nums2))  #Output: 0

nums3 = [1,1,1000000000]
print(minMoves(nums3))  #Output: 999999999
