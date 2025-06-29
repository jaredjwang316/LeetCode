# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 19:44:19 2025

@author: jwang

Problem Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must appear as many times as it shows in both arrays 
    and you may return the result in any order.
"""

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    freq_nums1 = dict()
    for n in nums1:
        if n not in freq_nums1:
            freq_nums1[n] = 1
        else:
            freq_nums1[n] += 1
    
    freq_nums2 = dict()
    for n in nums2:
        if n not in freq_nums2:
            freq_nums2[n] = 1
        else:
            freq_nums2[n] += 1

    intersect = []
    if len(nums1) < len(nums2):
        for n in nums1:
            if n in nums2 and intersect.count(n) < min(freq_nums1[n], freq_nums2[n]):
                intersect.append(n)
    else:
        for n in nums2:
            if n in nums1 and intersect.count(n) < min(freq_nums1[n], freq_nums2[n]):
                intersect.append(n)
    
    return intersect

nums1 = [1,2,2,1]
nums2 = [2,2]
print("Intersection of", nums1, "and", nums2, "is", intersect(nums1, nums2)) 


nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print("Intersection of", nums3, "and", nums4, "is", intersect(nums3, nums4))

nums5 = [1,2]
nums6 = [1,1]
print("Intersection of", nums5, "and", nums6, "is", intersect(nums5, nums6))



