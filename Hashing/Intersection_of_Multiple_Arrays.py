"""
Problem Description:
    - Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return 
    the list of integers that are present in each array of nums sorted in ascending order. 

Constraints:
    - 1 <= nums.length <= 1000
    - 1 <= sum(nums[i].length) <= 1000
    - 1 <= nums[i][j] <= 1000
    - All the values of nums[i] are unique.
"""

def intersection(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    num_freq = dict()

    set_list = list()
    for array in nums:
        set_list.append(set(array))
    

    for sets in set_list:
        for el in sets:
            if el not in num_freq:
                num_freq[el] = 1
            else:
                num_freq[el] += 1
    
    result = list()
    for k,v in num_freq.items():
        if v == len(nums):
            result.append(k)
    
    result.sort()
    return result

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums))  # Output: [3, 4]

nums2 = [[1,2,3],[4,5,6]]
if len(intersection(nums2)) == 0:
    print("No intersection found")  # Output: No intersection found