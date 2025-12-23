# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 19:44:59 2025

@author: jwang

Problem Description:
    Given a 1-indexed array of integers numbers that is already sorted in 
    non-decreasing order, find two numbers such that they add up to a specific 
    target number. Let these two numbers be numbers[index1] and numbers[index2] 
    where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an
    integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not 
    use the same element twice.
    Your solution must use only constant extra space.

Constraints:
    
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(numbers) - 1

    while(left < right):
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] < target - numbers[right]:
            left += 1
        else:
            right -= 1
    
    return []

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))  #[1, 2]

numbers2 = [2,3,4]
target2 = 6
print(twoSum(numbers2, target2))    #[1, 3]

numbers3 = [-1,0]
target3 = -1
print(twoSum(numbers3, target3))    #[1, 2]