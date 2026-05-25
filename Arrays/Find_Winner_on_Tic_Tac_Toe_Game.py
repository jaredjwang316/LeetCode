"""
Problem Description:
    * Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
        - Players take turns placing characters into empty squares ' '.
        - The first player A always places 'X' characters, while the second player B always places 'O' characters.
        - 'X' and 'O' characters are always placed into empty squares, never on filled ones.
        - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
        - The game also ends if all squares are non-empty.
        - No more moves can be played if the game is over.
    
    * Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on 
    grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return 
    "Draw". If there are still movements to play return "Pending".

    * You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, 
    and A will play first.
"""

def isWin(board, row, col):
    for r in range(len(board)): #check if there is a row filled with the same non-empty characters
        if board[r][0] != ' ' and board[r][0] == board[r][1] == board[r][2]:
            return True
    
    for c in range(len(board[0])):  #check if there is a column filled with the same non-empty characters
        if board[0][c] != ' ' and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
            return True
    
    if row == col and board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]: #diagonal 1 from left to right
        return True
    
    if row + col == 2 and board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]: #diagonal 2 from right to left
        return True

    return False

def tictactoe(moves):
    """
    :type moves: List[List[int]]
    :rtype: str
    """
    board = []
    for r in range(3):
        subList = []
        for c in range(3):
            subList.append(' ')
        board.append(subList)
    
    for m in range(len(moves)):
        if m % 2 == 0:   #A's turn since A always play first
            board[ moves[m][0] ][ moves[m][1] ] = 'X'
        else:
            board[ moves[m][0] ][ moves[m][1] ] = 'O'
        
        if isWin(board, moves[m][0], moves[m][1]) == True:
            if m % 2 == 0:
                return 'A'
            else:
                return 'B'

    if len(moves) == 9:
        return "Draw"
    return "Pending"

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(tictactoe(moves)) #Output: "A"

moves2 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(tictactoe(moves2)) #Output: "B"

moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(tictactoe(moves3)) #Output: "Draw"