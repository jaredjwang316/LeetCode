"""
Problem Description:
    - Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that 
    occurs more than 25% of the time, return that integer.

Constraints:
    - 1 <= arr.length <= 10^4
    - 0 <= arr[i] <= 10^5
"""

def findSpecialInteger(arr):
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
            if len(arr) < 4 * count:
                return arr[i]
        else:
            count = 1
    
    return arr[0]

arr1 = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr1))  #Output: 6

arr2 = [1,1]
print(findSpecialInteger(arr2))  #Output: 1

arr3 = [1]
print(findSpecialInteger(arr3))  #Output: 1

arr4 = [1,1,2,2,3,3,3,3]
print(findSpecialInteger(arr4))  #Output: 3