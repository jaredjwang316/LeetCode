# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 09:48:32 2025

@author: jwang

Problem Description:
    - Alice and Bob have a different total number of candies. You are given two 
    integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of 
    candies of the ith box of candy that Alice has and bobSizes[j] is the number 
    of candies of the jth box of candy that Bob has.
    - Since they are friends, they would like to exchange one candy box each so 
    that after the exchange, they both have the same total amount of candy. The 
    total amount of candy a person has is the sum of the number of candies 
    in each box they have.
    - Return an integer array answer where answer[0] is the number of candies in 
    the box that Alice must exchange, and answer[1] is the number of candies in 
    the box that Bob must exchange. If there are multiple answers, you may 
    return any one of them. It is guaranteed that at least one answer exists.

Important Constraints:
    1 <= aliceSizes.length, bobSizes.length <= 104
    1 <= aliceSizes[i], bobSizes[j] <= 105
    Alice and Bob have a different total number of candies.
    There will be at least one valid answer for the given input.
"""

def fairCandySwap(aliceSizes, bobSizes):
    """
    :type aliceSizes: List[int]
    :type bobSizes: List[int]
    :rtype: List[int]
    """
    
    totalAlice = 0
    for a in aliceSizes:
        totalAlice += a
    
    totalBob = 0
    for b in bobSizes:
        totalBob += b
    
    for a in aliceSizes:
        if a + (totalBob - totalAlice) // 2 in bobSizes:
            return [a, a + (totalBob - totalAlice) // 2 ]

    return -1

aliceSizes = [1,1] 
bobSizes = [2,2]
print(fairCandySwap(aliceSizes, bobSizes))  #[1,2]

aliceSizes2 = [1,2]
bobSizes2 = [2,3]
print(fairCandySwap(aliceSizes2, bobSizes2))    #[1,2]

aliceSizes3 = [2]
bobSizes3 = [1,3]
print(fairCandySwap(aliceSizes3, bobSizes3))    #[2, 3]

aliceSizes4 = [1,2,5]
bobSizes4 = [2,4]
print(fairCandySwap(aliceSizes4, bobSizes4))    #[5, 4]