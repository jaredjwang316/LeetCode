"""
Problem Description:
    - You are given an array of integers stones where stones[i] is the weight of the ith stone.
    - We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash 
    them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
        - If x == y, both stones are destroyed, and
        - If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    - At the end of the game, there is at most one stone left.
    - Return the weight of the last remaining stone. If there are no stones left, return 0.

Constraints:
    - 1 <= stones.length <= 30
    - 1 <= stones[i] <= 1000
"""

def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    while(len(stones) > 1):
        stones.sort()
        if stones[-1] == stones[-2]:    #if the two heaviest stones are equal in weight, both get destroyed
            stones.pop()
            stones.pop()
        else:
            newStone = stones[-1] - stones[-2]  # stone of weight y has new weight y - x.
            stones.pop()
            stones.pop()
            stones.append(newStone)
    
    if len(stones) == 1:
        return stones[0]
    return 0    #no stones left

stones = [2,7,4,1,8,1]
#Output: 1 -> We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then, 
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then we combine 2 and 1 to get 1 
# so the array converts to [1,1,1] then we combine 1 and 1 to get 0 so the array converts to [0,1] then 
# we combine 0 and 1 to get 1 so the array converts to [1] then that's the value of the last stone.
print(lastStoneWeight(stones))   

stones2 = [1]
print(lastStoneWeight(stones2))   #1 -> There's only one stone, so we return its weight.