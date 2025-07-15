# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 14:55:49 2025

@author: jwang

Problem Description:
    There is a robot on an m x n grid. The robot is initially located at the 
    top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
    corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right 
    at any point in time.
    Given the two integers m and n, return the number of possible unique paths 
    that the robot can take to reach the bottom-right corner.
    
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Constraints:
    1 <= m, n <= 100
"""

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = []

    for i in range(m):
        sub_list = []
        for j in range(n):
            sub_list.append(1)
        dp.append(sub_list)
    
    for i in range(1, m):
        for j in range(1, n):
            (dp[i])[j] = (dp[i - 1])[j] + (dp[i])[j - 1]
    
    return dp[m - 1][n - 1]

m = 3
n = 7
print(uniquePaths(m, n))    #28

m2 = 3
n2 = 2
#From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
print(uniquePaths(m2, n2))  #3
