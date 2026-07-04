"""
Problem Description:
    - You are given a string s consisting of n characters which are either 'X' or 'O'.
    - A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note 
    that if a move is applied to the character 'O', it will stay the same.
    - Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Constraints:
    - 3 <= s.length <= 1000
    - s[i] is either 'X' or 'O'.
"""

def minimumMoves(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    count_moves = 0

    while(i < len(s)):
        if s[i] == "X":
            i += 3
            count_moves += 1
        else:
            i += 1

    return count_moves

s = "XXX"
print(minimumMoves(s))  # Output: 1

s2 = "XXOX"
print(minimumMoves(s2))  # Output: 2

s3 = "OOOO"
print(minimumMoves(s3))  # Output: 0

s4 = "OXOX"
print(minimumMoves(s4))  # Output: 1

s5 = "XXXXX"
print(minimumMoves(s5))  # Output: 2

