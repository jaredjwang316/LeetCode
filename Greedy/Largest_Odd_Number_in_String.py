"""
Problem Description:
    - You are given a string num, representing a large integer. Return the largest-valued odd integer 
    (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer 
    exists.  A substring is a contiguous sequence of characters within a string.

Constraints:
    - 1 <= num.length <= 10^5
    - num only consists of digits and does not contain any leading zeros.
"""

def largestOddNumber(num):
    """
    :type num: str
    :rtype: str
    """
    index = -2

    for i in range(len(num) - 1, -1, -1):
        if ord(num[i]) % 2 == 1:
            index = i
            break
    
    if index == -2:
        return ""
    
    return num[0:index + 1]

num = "52"
print(largestOddNumber(num))  # Output: "5"

num2 = "4206"
if largestOddNumber(num2) == "":
    print("No odd integer exists in the string.")  # Output: "No odd integer exists in the string."

num3 = "35427"
print(largestOddNumber(num3))  # Output: "35427"
