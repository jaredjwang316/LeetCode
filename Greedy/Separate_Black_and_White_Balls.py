"""
Problem Description:
    - There are n balls on a table, each ball has a color black or white.
    - You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white 
    balls, respectively.
    - In each step, you can choose two adjacent balls and swap them.
    - Return the minimum number of steps to group all the black balls to the right and all the 
    white balls to the left.

Constraints:
    - 1 <= n == s.length <= 10^5
    - s[i] is either '0' or '1'.
"""

def minimumSteps(s):
    """
    :type s: str
    :rtype: int
    """
    count_ones = 0
    swap_left_zeros = 0

    for ch in s:
        if ch == "1":
            count_ones += 1
        elif ch == "0":
            # To move the current white ball to the left, we must swap count_ones number of times, which is the number of ones that occurred before the current ball
            swap_left_zeros += count_ones
    
    return swap_left_zeros

s = "101"
print(minimumSteps(s))  #Output: 1

s2 = "100"
print(minimumSteps(s2)) #Output: 2

s3 = "0111"
print(minimumSteps(s3)) #Output: 0