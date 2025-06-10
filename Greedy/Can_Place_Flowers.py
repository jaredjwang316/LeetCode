# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 14:38:41 2025

@author: jwang

Problem Description:
    You have a long flowerbed in which some of the plots are planted, and some 
    are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means 
    empty and 1 means not empty, and an integer n, return true if n new flowers 
    can be planted in the flowerbed without violating the no-adjacent-flowers 
    rule and false otherwise.

Important Constraints:
    - 1 <= flowerbed.length <= 2 * 104
    - flowerbed[i] is 0 or 1.
    - There are no two adjacent flowers in flowerbed.
    - 0 <= n <= flowerbed.length

"""

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    
    if n == 0:  #test cases are designed such that there are no two adjacent flowers in flowerbed.
        return True
    
    if len(flowerbed) == 1: #edge case: 1 plot in flowerbed
        if flowerbed[0] == 0:
            if n == 1:
                return True
            else:
                return False
        else:
            return False

    for f in range(len(flowerbed)):
        if f == 0 and flowerbed[f] == 0 and flowerbed[f + 1] == 0:
            flowerbed[f] = 1
            n -= 1
        if f == len(flowerbed) - 1 and flowerbed[f] == 0 and flowerbed[f - 1] == 0:
            flowerbed[f] = 1
            n -= 1

        if flowerbed[f] == 0 and flowerbed[f - 1] == 0 and flowerbed[f + 1] == 0:
            flowerbed[f] = 1
            n -= 1
    
    if n <= 0:
        return True
    
    return False

flowerbed = [1,0,0,0,1]
n = 1
print("Can", n, "flowers be planted in", flowerbed, "such that the " 
      "no-adjacent-flowers rule is not violated?", canPlaceFlowers(flowerbed, n))    #True

flowerbed2 = [1,0,0,0,1]
n2 = 2
print("Can", n2, "flowers be planted in", flowerbed2, "such that the " 
      "no-adjacent-flowers rule is not violated?", canPlaceFlowers(flowerbed2, n2))  #False

flowerbed3 = [0]
n3 = 1
print("Can", n2, "flowers be planted in", flowerbed3, "such that the " 
      "no-adjacent-flowers rule is not violated?", canPlaceFlowers(flowerbed3, n3))  #True
