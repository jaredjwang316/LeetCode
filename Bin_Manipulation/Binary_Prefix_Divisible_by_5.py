"""
Problem Description:
    - You are given a binary array nums (0-indexed).
    - We define xi as the number whose binary representation is the subarray nums[0..i] 
    (from most-significant-bit to least-significant-bit).
        * For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.

    - Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
"""

def prefixesDivBy5(nums):
    """
    :type nums: List[int]
    :rtype: List[bool]
    """
    
    resulting_list = []

    count_ones = 0
    prefix_bin = 0

    flag = False
    for n in range(len(nums)):
        if nums[n] == 1:
            count_ones += 1
        
        if count_ones >= 1: 
            if nums[n] == 1:
                if flag == False:   
                    prefix_bin = prefix_bin + pow(2, count_ones - 1)
                else:   
                    prefix_bin = prefix_bin * 2
                    prefix_bin = prefix_bin + 1
            else:   
                flag = True
                prefix_bin = prefix_bin * 2

        if prefix_bin % 5 == 0:
            resulting_list.append(True)
        else:
            resulting_list.append(False)
    
    return resulting_list

print(prefixesDivBy5([0,1,1]))  #Output: [True, False, False]
print(prefixesDivBy5([1,1,1]))  #Output: [False, False, False]

nums3 = [1,1,0,0,0,1,0,0,1]
print(prefixesDivBy5(nums3))  #Output: [false,false,false,false,false,false,false,false,false]
