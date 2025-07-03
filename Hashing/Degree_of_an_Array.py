# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 11:49:04 2025

@author: jwang

Problem Description:
    Given a non-empty array of non-negative integers nums, the degree of this 
    array is defined as the maximum frequency of any one of its elements.

    Your task is to find the smallest possible length of a (contiguous) subarray 
    of nums, that has the same degree as nums.

Constraints:
    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.
"""

def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_freq = dict()

    for n in range(len(nums)):
        if nums[n] not in num_freq:
            num_freq[nums[n]] = [1, [n] ]   #frequency with the list of indices of where that element occurred
        else:
            position_occurrence = (num_freq[nums[n]])[1]
            position_occurrence.append(n)
            num_freq[nums[n]] = [ (num_freq[nums[n]])[0] + 1, position_occurrence]

    #print(num_freq)
    maxFreq = 0
    wanted_mode = nums[0]
    for v in num_freq.values():
        if v[0] > maxFreq:
            maxFreq = v[0]

    min_index_dist = pow(2, 31) - 1
    for k,v in num_freq.items():
        if v[0] == maxFreq:
            if (v[1])[len(v[1]) - 1] - (v[1])[0] < min_index_dist:
                min_index_dist = (v[1])[len(v[1]) - 1] - (v[1])[0]
                wanted_mode = k

    shortest_subarray = []
    count_mode_el = 0
    for n in nums:
        if n == wanted_mode:
            shortest_subarray.append(n)
            count_mode_el += 1
        elif count_mode_el >= maxFreq:
            break
        elif count_mode_el > 0:
            shortest_subarray.append(n)
    
    return len(shortest_subarray)

nums = [1,2,2,3,1]
print(findShortestSubArray(nums))   #2

nums2 = [1,2,2,3,1,4,2]
print(findShortestSubArray(nums2))  #6

nums3 = [1,3,2,2,3,1]
print(findShortestSubArray(nums3))  #2

nums4 = [2,1,1,2,1,3,3,3,1,3,1,3,2]
print(findShortestSubArray(nums4))  #7

