# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:50:24 2025

@author: jwang

Problem Description:
    - You are given an integer array cost where cost[i] is the cost of ith step on 
    a staircase. Once you pay the cost, you can either climb one or two steps.
    - You can either start from the step with index 0, or the step with index 1.
    - Return the minimum cost to reach the top of the floor.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

"""

def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """

    dp = []
    for c in cost:
        dp.append(c)
    
    for i in range(len(dp) - 3, -1, -1):
        dp[i] += min(dp[i + 1], dp[i + 2])
    
    return min(dp[0], dp[1])

cost = [10,15,20]
print(minCostClimbingStairs(cost))  #15

cost2 = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost2)) #6