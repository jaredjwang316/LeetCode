"""
Problem Description:
    - You are given a 0-indexed string s that has lowercase English letters in its even indices and 
    digits in its odd indices.
    - You must perform an operation shift(c, x), where c is a character and x is a digit, that returns 
    the xth character after c.
        * For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
    - For every odd index i, you want to replace the digit s[i] with the result of the 
    shift(s[i-1], s[i]) operation.
    - Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
    - Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of 
    the solution.

Constraints:
    - 1 <= s.length <= 100
    - s consists only of lowercase English letters and digits.
    - shift(s[i-1], s[i]) <= 'z' for all odd indices i.
"""

def shift(letter, shift_amount):
    return chr(ord(letter) + (ord(shift_amount) - 48) )

def replaceDigits(s):
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)
    for i in range(1, len(s_list), 2):
        s_list[i] = shift(s_list[i - 1], s_list[i])
    
    return "".join(s_list)

s = "a1c1e1"
print(replaceDigits(s))  # Output: "abcdef"

s2 = "a1b2c3d4e"
print(replaceDigits(s2))  # Output: "abbdcfdhe"