"""
Problem Description:
    - You are given a string s consisting only of the characters '0' and '1'. In one operation, you can 
    change any '0' to '1' or vice versa.
    - The string is called alternating if no two adjacent characters are equal. For example, the string 
    "010" is alternating, while the string "0100" is not.
    - Return the minimum number of operations needed to make s alternating.
"""

def minOperations(s):
    """
    :type s: str
    :rtype: int
    """
    count_flip1 = 0 #trying to flip to produce a string of 101010...
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == "0":
            count_flip1 += 1
        elif i % 2 == 1 and s[i] == "1":
            count_flip1 += 1

    count_flip2 = 0 #trying to flip to produce a string like 010101...
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == "1":
            count_flip2 += 1
        elif i % 2 == 1 and s[i] == "0":
            count_flip2 += 1
    
    return min(count_flip1, count_flip2)

s = "0100"
print(minOperations(s)) #Output: 1

s2 = "10"
print(minOperations(s2)) #Output: 0

s3 = "1111"
print(minOperations(s3)) #Output: 2

s4 = "10010100"
print(minOperations(s4)) #Output: 3