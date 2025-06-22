# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 10:28:41 2025

@author: jwang

Problem Description:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to 
    be validated according to the following rules:
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 
          1-9 without repetition.
    Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned rules.
      
Important Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    row_vals = []
    #traverse every row
    for r in range(9):
        row_vals = []
        for i in range(9):
            if board[r][i] != '.':
                if board[r][i] not in row_vals:
                    row_vals.append(board[r][i])
                else:
                    return False

    col_vals = []
    #traverse every column
    for c in range(9):
        col_vals = []
        for i in range(9):
            if board[i][c] != '.':
                if board[i][c] not in col_vals:
                    col_vals.append(board[i][c])
                else:
                    return False

    subSquare_vals = []
    unique_vals = []
    #check every 3x3 sub-boxes on the board
    for i in range(3):  #row-based traversal
        for j in range(3):
            unique_vals = []
            subSquare_vals.append(board[3 * i][3 * j])
            subSquare_vals.append(board[3 * i][3 * j + 1])
            subSquare_vals.append(board[3 * i][3 * j + 2])
            subSquare_vals.append(board[3 * i + 1][3 * j])
            subSquare_vals.append(board[3 * i + 1][3 * j + 1])
            subSquare_vals.append(board[3 * i + 1][3 * j + 2])
            subSquare_vals.append(board[3 * i + 2][3 * j])
            subSquare_vals.append(board[3 * i + 2][3 * j + 1])
            subSquare_vals.append(board[3 * i + 2][3 * j + 2])             
            for k in range(9):
                if subSquare_vals[k] != '.':
                    if subSquare_vals[k] not in unique_vals:
                        unique_vals.append(subSquare_vals[k])
                    else:
                        return False
            subSquare_vals = []



    return True 

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print("Is the board", board, "a valid Sudoku?", isValidSudoku(board))

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print("Is the board", board2, "a valid Sudoku?", isValidSudoku(board2))

board3 = [[".",".",".",".","5",".",".","1","."]
          ,[".","4",".","3",".",".",".",".","."]
          ,[".",".",".",".",".","3",".",".","1"]
          ,["8",".",".",".",".",".",".","2","."]
          ,[".",".","2",".","7",".",".",".","."]
          ,[".","1","5",".",".",".",".",".","."]
          ,[".",".",".",".",".","2",".",".","."]
          ,[".","2",".","9",".",".",".",".","."]
          ,[".",".","4",".",".",".",".",".","."]]
print("Is the board", board3, "a valid Sudoku?", isValidSudoku(board3))

