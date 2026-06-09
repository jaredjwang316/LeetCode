"""
Problem Description:
    - You're given strings jewels representing the types of stones that are jewels, and stones representing 
    the stones you have. Each character in stones is a type of stone you have. You want to know how many of 
    the stones you have are also jewels.
    - Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:
    - 1 <= jewels.length, stones.length <= 50
    - jewels and stones consist of only English letters.
    - All the characters of jewels are unique.
"""

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    if len(stones) == 0:
        return 0
    
    if stones[0] in jewels:
        return 1 + numJewelsInStones(jewels, stones[1:])
    return 0 + numJewelsInStones(jewels, stones[1:])

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))    #3

jewels2 = "z"
stones2 = "ZZ"
print(numJewelsInStones(jewels2, stones2))    #0

