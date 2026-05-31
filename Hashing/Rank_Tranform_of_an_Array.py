"""
Problem Description:
    - Given an array of integers arr, replace each element with its rank.
    - The rank represents how large the element is. The rank has the following rules:

        * Rank is an integer starting from 1.
        * The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
        * Rank should be as small as possible.
"""

def arrayRankTransform(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    unique_arr = list(set(arr))
    unique_arr.sort()

    rank_dict = dict()
    for i in range(len(unique_arr)):
        rank_dict[unique_arr[i]] = i + 1
    
    rank_results = []
    for num in arr:
        rank_results.append(rank_dict[num])
    
    return rank_results

arr = [40,10,20,30]
print(arrayRankTransform(arr))   # Output: [4,1,2,3]

arr2 = [100,100,100]
print(arrayRankTransform(arr2))  # Output: [1,1,1]

arr3 = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr3))  # Output: [5,3,4,2,8,6,7,1,3]

