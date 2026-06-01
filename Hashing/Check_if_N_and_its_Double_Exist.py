"""
Problem Description:
    - Given an array arr of integers, check if there exist two indices i and j such that :
        * i != j
        * 0 <= i, j < arr.length
        * arr[i] == 2 * arr[j]

Constraints:
    - 2 <= arr.length <= 500
    - -10^3 <= arr[i] <= 10^3
"""

def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """

    arr.sort()
    double_D = dict()
    for num in arr:
        if 2 * num in double_D.keys():
            return True
        if num % 2 == 0 and num // 2 in double_D.keys():
            return True
        
        double_D[num] = 0
    
    return False

arr = [10,2,5,3]
print("does there exist two indices i and j such that arr[i] == 2 * arr[j]?", checkIfExist(arr))  # expected output: True

arr2 = [3,1,7,11]
print("does there exist two indices i and j such that arr[i] == 2 * arr[j]?", checkIfExist(arr2))  # expected output: False

arr3 = [-10,12,-20,-8,15]
print("does there exist two indices i and j such that arr[i] == 2 * arr[j]?", checkIfExist(arr3))  # expected output: True

arr4 = [-16,-13,8]
print("does there exist two indices i and j such that arr[i] == 2 * arr[j]?", checkIfExist(arr4))  # expected output: False

arr5 = [0,0]
print("does there exist two indices i and j such that arr[i] == 2 * arr[j]?", checkIfExist(arr5))  # expected output: True

