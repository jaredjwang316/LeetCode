"""
Problem Description:
    - There are numBottles water bottles that are initially full of water. You can exchange numExchange empty 
    water bottles from the market with one full water bottle.
    - The operation of drinking a full water bottle turns it into an empty bottle.
    - Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Constraints:
    - 1 <= numBottles <= 100
    - 2 <= numExchange <= 100
"""

def exchangeRecursion(numBottles, numExchange):
    if numBottles < numExchange:    #we don't have enough empty bottles to exchange even one full water bottle
        return 0
    
    return numBottles // numExchange + exchangeRecursion(numBottles // numExchange + numBottles % numExchange, numExchange)

def numWaterBottles(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    return numBottles + exchangeRecursion(numBottles, numExchange)

numBottles = 9
numExchange = 3
print("maximum number of water bottles you can drink:", numWaterBottles(numBottles, numExchange))  # expected output: 13

numBottles2 = 15
numExchange2 = 4
print("maximum number of water bottles you can drink:", numWaterBottles(numBottles2, numExchange2))  # expected output: 19