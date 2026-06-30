"""
Problem Description:
    - A fancy string is a string where no three consecutive characters are equal.
    - Given a string s, delete the minimum possible number of characters from s to make it fancy.
    - Return the final string after the deletion. It can be shown that the answer will always be 
    unique.

Constraints:
    - 1 <= s.length <= 10^5
    - s consists only of lowercase English letters.
"""

def makeFancyString(s):
    """
    :type s: str
    :rtype: str
    """
    fancy_string = s[0]
    consecutive_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            consecutive_count += 1
            if consecutive_count < 3:
                fancy_string += s[i]
        else:
            fancy_string += s[i]
            consecutive_count = 1
    
    return fancy_string

s = "leeetcode"
print(makeFancyString(s))   #leetcode

s2 = "aaabaaaa"
print(makeFancyString(s2))  #aabaa

s3 = "aab"
print(makeFancyString(s3))  #aab