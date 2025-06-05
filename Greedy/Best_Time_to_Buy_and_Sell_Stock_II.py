# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 14:37:39 2025

@author: jwang

Problem:
    You are given an integer array prices where prices[i] is the 
    price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only 
    hold at most one share of the stock at any time. However, you can buy it 
    then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
         
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            maxProfit +=  prices[i] - prices[i - 1]
    
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices2 = [1,2,3,4,5]
print(maxProfit(prices2))

prices3 = [7,6,4,3,1]
print(maxProfit(prices3))

prices4 = [1]
print(maxProfit(prices4))