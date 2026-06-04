"""
Problem Description:
    - You are given two integer arrays of equal length target and arr. In one step, you 
    can select any non-empty subarray of arr and reverse it. You are allowed to make 
    any number of steps.
    - Return true if you can make arr equal to target or false otherwise.
"""

def canBeEqual(target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    target_freq = dict()
    for num in target:
        if num not in target_freq:
            target_freq[num] = 1
        else:
            target_freq[num] += 1

    arr_freq = dict()
    for num in arr:
        if num not in arr_freq:
            arr_freq[num] = 1
        else:
            arr_freq[num] += 1
    
    for k,v in arr_freq.items():
        if k not in target_freq:
            return False
        if v != target_freq[k]:
            return False
    
    return True

target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target, arr))   # Output: True

target2 = [7]
arr2 = [7]
print(canBeEqual(target2, arr2))   # Output: True

target3 = [3,7,9]
arr3 = [3,7,11]
print(canBeEqual(target3, arr3))   # Output: False