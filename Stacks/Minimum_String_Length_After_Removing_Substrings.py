"""
Problem Description:
    - You are given a string s consisting only of uppercase English letters.
    - You can apply some operations to this string where, in one operation, you can remove any occurrence 
    of one of the substrings "AB" or "CD" from s.
    - Return the minimum possible length of the resulting string that you can obtain.
    - Note that the string concatenates after removing the substring and could produce new "AB" or "CD" 
    substrings.

Constraints:
    - 1 <= s.length <= 100
    - s consists only of uppercase English letters.
"""

def minLength(s):
    """
    :type s: str
    :rtype: int
    """
    theStack = []

    for ch in s:
        if ch == "B" and len(theStack) > 0 and theStack[-1] == "A":
            theStack.pop()
        elif ch == "D" and len(theStack) > 0 and theStack[-1] == "C":
            theStack.pop()
        else:
            theStack.append(ch)
    
    return len(theStack)

s = "ABFCACDB"
print(minLength(s)) # Output: 2

s2 = "ACBBD"
print(minLength(s2)) # Output: 5