"""
Problem Description:
    - Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, 
    and all the 0's and all the 1's in these substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they occur.

Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is either '0' or '1'.
"""

def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    prev_consecutive_count = 0
    curr_consecutive_count = 1

    result = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_consecutive_count += 1
        else:
            result = result + min(prev_consecutive_count, curr_consecutive_count)
            prev_consecutive_count = curr_consecutive_count
            curr_consecutive_count = 1
    result = result + min(prev_consecutive_count, curr_consecutive_count)
    
    return result

s = "00110011"
print(countBinarySubstrings(s))   #6 -> The 6 substrings are "0011", "01", "1100", "10", "0011", and "01".

s2 = "10101"
print(countBinarySubstrings(s2))   #4 -> The 4 substrings are "10", "01", "10", and "01".

s3 = "001"
print(countBinarySubstrings(s3))   #1 

s4 = "0010"
print(countBinarySubstrings(s4))   #2 -> The 2 substrings are "01" and "10".

s5 = "00101"
print(countBinarySubstrings(s5))   #3 -> The 3 substrings are "01", "10", and "01".

s6 = "00111"
print(countBinarySubstrings(s6))   #2 -> The 2 substrings are "0011" and "01".