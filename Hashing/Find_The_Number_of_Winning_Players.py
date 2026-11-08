"""
Problem Description:
    - You are given an integer n representing the number of players in a game and a 2D array pick where 
    pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.
    - Player i wins the game if they pick strictly more than i balls of the same color. In other words,
        * Player 0 wins if they pick any ball.
        * Player 1 wins if they pick at least two balls of the same color.
        ...
        * Player i wins if they pick at least i + 1 balls of the same color.
    - Return the number of players who win the game.
    - Note that multiple players can win the game.

Constraints:
    - 2 <= n <= 10
    - 1 <= pick.length <= 100
    - pick[i].length == 2
    - 0 <= xi <= n - 1 
    - 0 <= yi <= 10
"""

def winningPlayerCount(n, pick):
    """
    :type n: int
    :type pick: List[List[int]]
    :rtype: int
    """
    #Nested dictionary
    #In the outer dictionary, the player is the key
    #In the inner dictionary, the ball color is the key and the value if the number of balls the player picked in that color
    player_ball = dict()

    for p in pick:
        if p[0] not in player_ball:
            player_ball[p[0]] = dict()
        
        if p[1] not in player_ball[p[0]]:
            (player_ball[p[0]])[p[1]] = 1
        else:
            (player_ball[p[0]])[p[1]] += 1

    count_winning_players = 0

    for player_num, ball_colors in player_ball.items():
        for ball_color, val in ball_colors.items():
            if val >= player_num + 1:
                count_winning_players += 1
                break

    return count_winning_players

n = 4
pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
print(winningPlayerCount(n, pick))  # 2, Player 0 and player 1 win the game, while players 2 and 3 do not win.

n2 = 5
pick2 = [[1,1],[1,2],[1,3],[1,4]]
print(winningPlayerCount(n2, pick2))    # 0, no player wins the game

n3 = 5
pick3 = [[1,1],[2,4],[2,4],[2,4]]
print(winningPlayerCount(n3, pick3))    #1, Player 2 wins the game by picking 3 balls with color 4.
