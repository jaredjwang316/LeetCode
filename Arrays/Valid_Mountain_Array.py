"""
Problem Description:
    - Given an array of integers arr, return true if and only if it is a valid mountain array.
    - Recall that arr is a mountain array if and only if:
        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
"""

def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if len(arr) < 3:
        return False
    
    stopIncreasing = False
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False
        elif arr[i] < arr[i - 1]:
            if i < 2:
                return False
            stopIncreasing = True
        else:
            if stopIncreasing == True:
                return False
    
    if stopIncreasing == False: #if decreasing never happened in the list
        return False
    return True

arr = [2,1]
print(validMountainArray(arr))  #False

arr2 = [3,5,5]
print(validMountainArray(arr2))  #False

arr3 = [0,3,2,1]
print(validMountainArray(arr3))  #True

arr4 = [0,1,2,3,4,5,6,7,8,9]
print(validMountainArray(arr4))  #False