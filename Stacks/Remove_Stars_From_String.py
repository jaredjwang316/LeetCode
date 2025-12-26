"""
You are given a string s, which contains stars *.

In one operation, you can:
    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters and stars *.
    The operation above can be performed on s.
"""

def removeStars(s):
    """
    :type s: str
    :rtype: str
    """
    theStack = []

    for ch in s:
        if ch == '*':
            theStack.pop()
        else:
            theStack.append(ch)
    
    result = ""
    for ch in theStack:
        result += ch
    return result

s = "leet**cod*e"
print(removeStars(s))   # "lecoe"

s2 = "erase*****"
if removeStars(s2) == "":
    print("Returns an empty String")