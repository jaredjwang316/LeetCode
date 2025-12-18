def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    inc = 1
    dec = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc = dec + 1
        elif nums[i] < nums[i - 1]:
            dec = inc + 1
    
    return max(inc, dec)

nums = [1,7,4,9,2,5]
print(wiggleMaxLength(nums))    #6

nums2 = [1,17,5,10,13,15,10,5,16,8]
print(wiggleMaxLength(nums2))   #7

nums3 = [1,2,3,4,5,6,7,8,9]
print(wiggleMaxLength(nums3))   #2


