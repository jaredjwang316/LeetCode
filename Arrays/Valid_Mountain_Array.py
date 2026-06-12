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
    
    isIncreasing = False
    isDecreasing = False

    if arr[1] > arr[0]:
        isIncreasing = True
    elif arr[1] < arr[0]:
        isDecreasing = True
    else:
        return False

    for i in range(2, len(arr), 1):
        if arr[i] > arr[i - 1]: #mountains first strictly increase, then strictly decrease
            if isDecreasing == True:    #check if decreased beforehand
                return False
            isIncreasing = True #indicate an increase happened 
        elif arr[i] < arr[i - 1]:
            if isIncreasing == False:   #if there was no increase beforehand, this array is not a mountain based on the definition of a mountain
                return False
            isDecreasing = True #indicate a decrease happened 
        else:
            return False

    if isDecreasing == False:
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