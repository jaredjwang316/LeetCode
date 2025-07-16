# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:36:41 2025

@author: jwang

Problem Description: 
    You are given an 8 x 8 matrix representing a chessboard. There is exactly 
    one white rook represented by 'R', some number of white bishops 'B', and 
    some number of black pawns 'p'. Empty squares are represented by '.'.

    A rook can move any number of squares horizontally or vertically (up, down, 
    left, right) until it reaches another piece or the edge of the board. A 
    rook is attacking a pawn if it can move to the pawn's square in one move.
    
    Note: A rook cannot move through other pieces, such as bishops or pawns. 
    This means a rook cannot attack a pawn if there is another piece blocking 
    the path.

    Return the number of pawns the white rook is attacking.
    
Constraints:
    board.length == 8
    board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'
"""

def numRookCaptures(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    rook_row = 0
    rook_col = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'R':  #identify the location of the rook
                rook_row = r
                rook_col = c

    count_vulnerable_pawns = 0

    #row checking for pawns on the same row of the rook, horizontal direction
    for c in range(rook_col - 1, -1, -1):   #horizontally left
        if board[rook_row][c] == 'B':   #rook cannot move through other pieces
            break
        if board[rook_row][c] == 'p':   #it can capture that pawn but cannot other pawns behind it
            count_vulnerable_pawns += 1
            break
    
    for c in range(rook_col + 1, len(board[rook_row])): #horizontally right
        if board[rook_row][c] == 'B':   #rook cannot move through other pieces
            break
        if board[rook_row][c] == 'p':   #it can capture that pawn but cannot other pawns behind it
            count_vulnerable_pawns += 1
            break
    
    #column checking for pawns on the same column of the rook, both up and down
    for r in range(rook_row - 1, -1, -1):   #vertically up
        if board[r][rook_col] == 'B':   #rook cannot move through other pieces
            break
        if board[r][rook_col] == 'p':   #it can capture that pawn but cannot other pawns behind it
            count_vulnerable_pawns += 1
            break
    
    for r in range(rook_row + 1, len(board)):   #vertically down
        if board[r][rook_col] == 'B':   #rook cannot move through other pieces
            break
        if board[r][rook_col] == 'p':   #it can capture that pawn but cannot other pawns behind it
            count_vulnerable_pawns += 1
            break            
    
    return count_vulnerable_pawns

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(numRookCaptures(board))   #3

board2 = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],
          [".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],
          [".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],
          [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(numRookCaptures(board2))   #0

board3 = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
          [".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],
          [".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],
          [".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(numRookCaptures(board3))  #3
