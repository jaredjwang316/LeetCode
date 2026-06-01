"""
Problem Description:
    - A shop is selling candies at a discount. For every two candies sold, 
    the shop gives a third candy for free.
    - The customer can choose any candy to take away for free as long as the cost of the 
    chosen candy is less than or equal to the minimum cost of the two candies bought.
        * For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer 
        buys candies with costs 2 and 3, they can take the candy with cost 1 for free, 
        but not the candy with cost 4.
    - Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, 
    return the minimum cost of buying all the candies.

Constraints:
    - 1 <= cost.length <= 100
    - 1 <= cost[i] <= 100
"""

def minimumCost(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    cost.sort(reverse = True)

    minimized_cost = 0
    for c in range(len(cost)):
        if (c + 1) % 3 != 0:
            minimized_cost += cost[c]
    
    return minimized_cost

cost = [1,2,3]
print("minimum cost of buying all candies:", minimumCost(cost))  # expected output: 5

cost2 = [6,5,7,9,2,2]
print("minimum cost of buying all candies:", minimumCost(cost2))  # expected output: 23

cost3 = [5,5]
print("minimum cost of buying all candies:", minimumCost(cost3))  # expected output: 10

cost4 = [1,2,3,4,5]
print("minimum cost of buying all candies:", minimumCost(cost4))  # expected output: 12