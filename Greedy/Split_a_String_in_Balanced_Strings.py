"""
Problem Description:
    - Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
    - Given a balanced string s, split it into some number of substrings such that:
        - Each substring is balanced.
    - Return the maximum number of balanced strings you can obtain.

Constraints:
    - 2 <= s.length <= 1000
    - s[i] is either 'L' or 'R'.
    - s is a balanced string.
"""

def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    count_consecutive_R = 0
    count_consecutive_S = 0

    maxSplit = 0
    for ch in s:
        if ch == 'R':
            count_consecutive_R += 1
            if count_consecutive_R == count_consecutive_S:
                maxSplit += 1
                count_consecutive_R = 0
                count_consecutive_S = 0
        else:
            count_consecutive_S += 1
            if count_consecutive_R == count_consecutive_S:
                maxSplit += 1
                count_consecutive_S = 0
                count_consecutive_R = 0
        
    return maxSplit

s = "RLRRLLRLRL"
print("maximum number of balanced strings:", balancedStringSplit(s))  # expected output: 4

s2 = "RLRRRLLRLL"
print("maximum number of balanced strings:", balancedStringSplit(s2))  # expected output: 2

s3 = "LLLLRRRR"
print("maximum number of balanced strings:", balancedStringSplit(s3))  # expected output: 1
