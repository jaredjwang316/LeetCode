# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 23:51:02 2025

@author: jwang

Problem Description:
    There are n children standing in a line. Each child is assigned a rating 
    value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:
        - Each child must have at least one candy.
        - Children with a higher rating get more candies than their neighbors.
    
    Return the minimum number of candies you need to have to distribute the 
    candies to the children.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4
"""

def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """

    candy_distribution = []
    for i in range(len(ratings)):
        candy_distribution.append(1)    #all children must have at least one candy
    
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]: #compare current rating with left neighbor's rating
            candy_distribution[i] = (candy_distribution[i - 1] + 1)

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]: #compare current rating with right neighbor's rating
            candy_distribution[i] = max(candy_distribution[i], candy_distribution[i + 1] + 1)

    return sum(candy_distribution) 

ratings = [1,0,2]
print(candy(ratings))   #5

ratings2 = [1,2,2]
print(candy(ratings2))  #4

ratings3 = [1,3,2,2,1]
print(candy(ratings3))  #7

ratings4 = [1,2,87,87,87,2,1]
print(candy(ratings4))  #13