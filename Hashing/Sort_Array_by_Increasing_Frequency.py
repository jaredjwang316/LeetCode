"""
Problem Description:
    - Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple 
    values have the same frequency, sort them in decreasing order.  Return the sorted array.

Constraints:
    - 1 <= nums.length <= 100
    - -100 <= nums[i] <= 100
"""

from collections import Counter

def frequencySort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    num_freq = Counter(nums)

    # sort based on increasing frequency.  For values that have same frequency, sort in decreasing order
    adjust = sorted(num_freq.items(), key = lambda x: (x[1], -x[0]))

    resulting_list = []
    for tup in adjust:
        for iteration in range(tup[1]):
            resulting_list.append(tup[0])

    return resulting_list

nums = [1,1,2,2,2,3]
print(frequencySort(nums))  # [3,1,1,2,2,2]

nums2 = [2,3,1,3,2]
print(frequencySort(nums2)) # [1,3,3,2,2]

nums3 = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums3)) # [5,-1,4,4,-6,-6,1,1,1]