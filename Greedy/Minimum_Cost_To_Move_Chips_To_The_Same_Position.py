"""
Problem Description:
    - We have n chips, where the position of the ith chip is position[i].
    - We need to move all the chips to the same position. In one step, we can change the position of the ith chip 
    from position[i] to:
        - position[i] + 2 or position[i] - 2 with cost = 0.
        - position[i] + 1 or position[i] - 1 with cost = 1.
    - Return the minimum cost needed to move all the chips to the same position.

Constraints:
    - 1 <= position.length <= 100
    - 1 <= position[i] <= 10^9
"""

def minCostToMoveChips(position):
    """
    :type position: List[int]
    :rtype: int
    """
    count_evens = 0
    count_odds = 0
    for num in position:
        if num % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    
    if count_evens > count_odds:    #total number of moves required to move chips from odd positions to even positions is less than the total number of moves required to move chips from even positions to odd positions
        return count_odds

    return count_evens

position = [1,2,3]
print(minCostToMoveChips(position))   # 1

position2 = [2,2,2,3,3]
print(minCostToMoveChips(position2))  # 2

position3 = [1,1000000000]
print(minCostToMoveChips(position3))  # 1

position4 = [2,3,3]
print(minCostToMoveChips(position4))  # 1

position5 = [3,3,1,2,2]
print(minCostToMoveChips(position5))  # 2

position6 = [6,4,7,8,2,10,2,7,9,7]
print(minCostToMoveChips(position6))  # 4

