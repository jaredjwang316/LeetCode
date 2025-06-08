# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 17:36:40 2025

@author: jwang

Problem Description:
    You are given an array prices where prices[i] is the 
    price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock 
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    buy = 0
    sell = 1

    maxProfit = 0
    while (sell < len(prices)):
        if prices[sell] > prices[buy]:
            maxProfit = max(maxProfit, prices[sell] - prices[buy])
        else:
            buy = sell
        
        sell += 1
    
    return maxProfit

prices = [7,1,5,3,6,4]
print("the maximum profit you can get here =", maxProfit(prices))

prices2 = [7,6,4,3,1]
print("the maximum profit you can get here =", maxProfit(prices2))
