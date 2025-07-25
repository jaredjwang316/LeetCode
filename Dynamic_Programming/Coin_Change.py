# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 21:45:18 2025

@author: jwang

Problem Description:
    - You are given an integer array coins representing coins of different 
    denominations and an integer amount representing a total amount of money.
    - Return the fewest number of coins that you need to make up that amount. If 
    that amount of money cannot be made up by any combination of the coins, return -1.
    - You may assume that you have an infinite number of each kind of coin.

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 104
"""

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = []
    for i in range(amount + 1):
        if i == 0:
            dp.append(0)    #no coins needed to make amount 0
        else:
            dp.append(amount + 1)
    
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    
    if dp[amount] == amount + 1:
        return -1
    
    return dp[amount]

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))    #3 -> 11 = 5 + 5 + 1

coins2 = [2]
amount2 = 3
print(coinChange(coins2, amount2))  #-1 

coins3 = [1]
amount3 = 0
print(coinChange(coins3, amount3))  #0 

coins4 = [186,419,83,408]
amount4 = 6249
print(coinChange(coins4, amount4))  #20

