"""
Problem Description:
    - Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
        * Alice starts by removing exactly 10 stones on her first turn.
        * For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
    - The player who cannot make a move loses the game.
    - Given a positive integer n, return true if Alice wins the game and false otherwise.

Constraints:
    - 1 <= n <= 50
"""

def canAliceWin(n):
    """
    :type n: int
    :rtype: bool
    """
    aliceWin = False

    stones_removed = 10 #Alice goes first and starts by removing exactly 10 stones on her first turn.
    
    while(n >= stones_removed): #while a move can be made
        n = n - stones_removed 

        stones_removed -= 1 # For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.

        if aliceWin == False:
            aliceWin = True
        else:
            aliceWin = False
    
    return aliceWin

n = 12
print(canAliceWin(n)) # Output: True

n2 = 1
print(canAliceWin(n2)) # Output: False