"""
Problem Description:
    - Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] 
    (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
    - Return the maximum difference. If no such i and j exists, return -1.

Constraints:
    - n == nums.length
    - 2 <= n <= 1000
    - 1 <= nums[i] <= 10^9
"""

def maximumDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxDiff = -1

    minEncountered = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] < minEncountered[-1]:
            minEncountered.append(nums[i])
        else:
            minEncountered.append(minEncountered[-1])
    
    for j in range(1, len(nums)):
        if nums[j] - minEncountered[j - 1] > 0:
            maxDiff =  max(maxDiff, nums[j] - minEncountered[j - 1])
    
    return maxDiff

nums = [7,1,5,4]
print(maximumDifference(nums))  # Output: 4

nums2 = [9,4,3,2]
print(maximumDifference(nums2))  # Output: -1

nums3 = [1,5,2,10]
print(maximumDifference(nums3))  # Output: 9

nums4 = [87,68,91,86,58,63,43,98,6,40]
print(maximumDifference(nums4)) # Output: 55

nums5 = [999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,
         824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,
         583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,
         235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
print(maximumDifference(nums5)) # Output: -1