"""
Problem Description:
    You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your 
    movement on a number line starting from the origin 0.

    In the ith move, you can choose one of the following directions:
        - move to the left if moves[i] = 'L' or moves[i] = '_'
        - move to the right if moves[i] = 'R' or moves[i] = '_'

    Return the distance from the origin of the furthest point you can get to after n moves.

Constraints:
    1 <= moves.length == n <= 50
    moves consists only of characters 'L', 'R' and '_'.
"""

def furthestDistanceFromOrigin(moves):
    """
    :type moves: str
    :rtype: int
    """
    pos = 0 #starting position is at origin 0
    count_left = 0
    count_right = 0
    count_underscore = 0

    for move in moves:
        if move == 'L':
            count_left += 1
            pos -= 1
        elif move == 'R':
            count_right += 1
            pos += 1
        else:
            count_underscore += 1
    
    if count_underscore == len(moves):
        return count_underscore
    
    if count_right < count_left:
        pos -= count_underscore #moving left, letting all underscores be L, is more optimal resulting in further distance
    elif count_right > count_left:
        pos += count_underscore #moving right, letting all underscores be R, is more optimal resulting in further distance
    else:
        pos += count_underscore #moving right and moving left, letting all underscores to be R or L is equally optimal, so we let all underscores be R
    
    return abs(pos) #we want distance from origin, not displacement

moves = "L_RL__R"
print(furthestDistanceFromOrigin(moves))    #3

moves2 = "_R__LL_"
print(furthestDistanceFromOrigin(moves2))    #5

moves3 = "____"
print(furthestDistanceFromOrigin(moves3))    #4

moves4 = "LRLRLRLRLR"
print(furthestDistanceFromOrigin(moves4))    #0

moves5 = "LLLRRRR"
print(furthestDistanceFromOrigin(moves5))    #1

moves6 = "LLL__RRRR"
print(furthestDistanceFromOrigin(moves6))    #3