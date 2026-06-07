"""
Problem Description:
    - You are given a string s.  Your task is to remove all digits by doing this operation repeatedly:
        * Delete the first digit and the closest non-digit character to its left.

    - Return the resulting string after removing all digits.
    - Note that the operation cannot be performed on a digit that does not have any non-digit 
    character to its left.

Constraints:
    - 1 <= s.length <= 100
    - s consists only of lowercase English letters and digits.
    - The input is generated such that it is possible to delete all digits.
"""

def clearDigits(s):
    """
    :type s: str
    :rtype: str
    """
    stringStack = []

    for ch in s:
        if ord(ch) >= 48 and ord(ch) <= 57: #if the character is a digit
            if len(stringStack) > 0:
                stringStack.pop()
        else:
            stringStack.append(ch)
    
    return "".join(stringStack)

s = "abc"
print(clearDigits(s))   # Output: "abc" because there are no digits in the string.

s2 = "cb34"
if len(clearDigits(s2)) == 0:
    print("Empty String")   # Output: "Empty String" because all characters are removed.

s3 = "a1b2c3"
if len(clearDigits(s3)) == 0:
    print("Empty String again")   # Output: "Empty String" because all characters are removed.