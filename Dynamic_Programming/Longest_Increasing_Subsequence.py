def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dp = []
    for i in range(len(nums)):
        dp.append(1)    #1 is the minimum length a subsequence can be

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    
    return max(dp)


nums = [10,9,2,5,3,7,101,18]
print("The length of the longest increasing subsequence is,", lengthOfLIS(nums))

nums1 = [0,1,0,3,2,3]
print("The length of the longest increasing subsequence is,", lengthOfLIS(nums1))

nums2 = [7,7,7,7,7,7,7]
print("The length of the longest increasing subsequence is,", lengthOfLIS(nums2))