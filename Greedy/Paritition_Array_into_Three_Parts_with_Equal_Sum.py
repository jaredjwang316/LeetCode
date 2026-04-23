"""
Problem Description:
    Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

    Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == 
    arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Constraints:
    3 <= arr.length <= 5 * 10^4
    -10^4 <= arr[i] <= 10^4
"""

def canThreePartsEqualSum(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    
    totalSum = sum(arr)
    if totalSum % 3 != 0:
        return False
    
    subSum = 0
    partition_count = 0
    for i in range(len(arr)):
        subSum = subSum + arr[i]
        if subSum == (totalSum // 3):
            partition_count += 1
            subSum = 0  #reset the subsum for next partitioning
            if partition_count == 3:
                return True

    return False

arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(canThreePartsEqualSum(arr))   #True: 0 + 2 + 1 = -6 + 6 + -7 + 9 + 1 = 2 + 0 + 1

arr2 = [0,2,1,-6,6,7,9,-1,2,0,1]
print(canThreePartsEqualSum(arr2))   #False

arr3 = [3,3,6,5,-2,2,5,1,-9,4]
print(canThreePartsEqualSum(arr3))   #True: 3 + 3 = 6 = 5 + -2 + 2 + 5 + 1 + -9 + 4

arr4 = [0,0,0,0]
print(canThreePartsEqualSum(arr4))   #True: 0 = 0 = 0 + 0

arr5 = [1,-1,1,-1]
print(canThreePartsEqualSum(arr5))   #False: 1 + -1 = 0, but the remaining part is 1 + -1 = 0, which is not equal to the first two parts.