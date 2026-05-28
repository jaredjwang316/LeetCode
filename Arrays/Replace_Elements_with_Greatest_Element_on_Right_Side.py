"""
Problem Description:
    - Given an array arr, replace every element in that array with the greatest element among the elements 
    to its right, and replace the last element with -1.  After doing so, return the array.

Constraints:
    - 1 <= arr.length <= 10^4
    - 1 <= arr[i] <= 10^5
"""

def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    
    greatest_right_element = -1
    for i in range(len(arr) - 1, -1, -1):
        curr_element = arr[i]
        arr[i] = greatest_right_element
        greatest_right_element = max(greatest_right_element, curr_element)
    
    return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))  #Output: [18,6,6,6,1,-1]

arr2 = [400]
print(replaceElements(arr2))  #Output: [-1]
