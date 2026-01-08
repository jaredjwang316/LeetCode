"""
Problem Description:
    You are given an integer array prices where prices[i] is the price of the ith item in a shop.

    There is a special discount for items in the shop. If you buy the ith item, then you will receive 
    a discount equivalent to prices[j] where j is the minimum index such that j > i and 
    prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

    Return an integer array answer where answer[i] is the final price you will pay for the ith item 
    of the shop, considering the special discount.

Constraints:
    1 <= prices.length <= 500
    1 <= prices[i] <= 10^3
 
"""

def finalPrices(prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """
    indexStack = []

    for p in range(len(prices)):
        while (len(indexStack) > 0 and prices[p] <= prices[indexStack[-1]]):
            prices[indexStack[-1]] -= prices[p]
            indexStack.pop()
        indexStack.append(p)
    return prices

print(finalPrices([8,4,6,2,3])) #[4,2,4,2,3]

print(finalPrices([1,2,3,4,5])) #[1,2,3,4,5]

print(finalPrices([10,1,1,6])) #[9,0,1,6]