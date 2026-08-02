"""
Problem Description:
    - There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 
    0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
    - Return the maximum distance between two houses with different colors.
    - The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

Constraints:
    - n == colors.length
    - 2 <= n <= 100
    - 0 <= colors[i] <= 100
    - Test data are generated such that at least two houses have different colors.
"""

def maxDistance(colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    maxDistance = 0

    for i in range(1, len(colors)):
        if colors[i] != colors[0]:
            maxDistance = max(maxDistance, i)
    
    for i in range(len(colors) - 1):
        if colors[i] != colors[-1]:
            maxDistance = max(maxDistance, len(colors) - 1 - i)
    
    return maxDistance

colors = [1,1,1,6,1,1,1]
print(maxDistance(colors))  # Output: 3

colors2 = [1,8,3,8,3]
print(maxDistance(colors2))  # Output: 4

colors3 = [0,1]
print(maxDistance(colors3))  # Output: 1