"""
Problem Description:
    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below. More formally, if 
    you are on index i on the current row, you may move to either index i or index i + 1 on 
    the next row.

Important Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4
"""

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = triangle

    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
    
    return dp[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))   #11

triangle2 = [[-10]]
print(minimumTotal(triangle2))  #-10