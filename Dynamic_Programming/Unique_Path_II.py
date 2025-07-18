# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:50:24 2025

@author: jwang

Problem Description:
    - You are given an m x n integer array grid. There is a robot initially located 
    at the top-left corner (i.e., grid[0][0]). The robot tries to move to the 
    bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move 
    either down or right at any point in time.
    
    - An obstacle and space are marked as 1 or 0 respectively in grid. A path that 
    the robot takes cannot include any square that is an obstacle.
    
    - Return the number of possible unique paths that the robot can take to reach 
    the bottom-right corner.
    
    - The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.

"""

def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """  
    if obstacleGrid[0][0] == 1: #in this case, robot is starting on an obstacle, and obstacles cannot be touched
        return 0
    
    dp = []
    for r in range(len(obstacleGrid)):
        sub_list = []
        for c in range(len(obstacleGrid[r])):
            sub_list.append(1)
        dp.append(sub_list)
    
    for r in range(len(dp)):
        for c in range(len(dp[r])):
            top = 0
            left = 0
            if r == 0 and c == 0:
                continue
            
            if obstacleGrid[r][c] == 1: #obstacle grid cannot be touched
                dp[r][c] = 0
                continue
            
            if r > 0: #not the topmost row, then top exists
                top = dp[r - 1][c]
            
            if c > 0: #not the leftmost column, then left exists
                left = dp[r][c - 1]

            dp[r][c] = top + left
    
    return dp[len(dp) - 1][len(dp[0]) - 1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))   #2

obstacleGrid2 = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid2))  #1

obstacleGrid3 = [[1]]
print(uniquePathsWithObstacles(obstacleGrid3))  #0
