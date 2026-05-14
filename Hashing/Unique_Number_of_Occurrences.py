"""
Problem Description:
    - Given an array of integers arr, return true if the number of occurrences of each value in the 
    array is unique or false otherwise.

Constraints:
    - 1 <= arr.length <= 1000
    - -1000 <= arr[i] <= 1000
"""

def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    num_freq = dict()

    for num in arr:
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1
    
    freq_list = []
    for val in num_freq.values():
        freq_list.append(val)
    
    freq_list.sort()
    for f in range(1, len(freq_list)):
        if freq_list[f] == freq_list[f - 1]:
            return False
    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))   # True

arr2 = [1,2]
print(uniqueOccurrences(arr2))  # False

arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr3))  # True

arr4 = [26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]
print(uniqueOccurrences(arr4))  # False

arr5 = [1,1,1,3]
print(uniqueOccurrences(arr5))  # True