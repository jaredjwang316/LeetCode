"""
Problem Description:
    Given a string s, you have two types of operation:
        - Choose an index i in the string, and let c be the character in position i. Delete the closest 
        occurrence of c to the left of i (if exists).
        - Choose an index i in the string, and let c be the character in position i. Delete the closest 
        occurrence of c to the right of i (if exists).
    Your task is to minimize the length of s by performing the above operations zero or more times.
    Return an integer denoting the length of the minimized string.

Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters.
"""

def minimizedStringLength(s):
    """
    :type s: str
    :rtype: int
    """
    char_freq = dict()
    for ch in s:
        if ch not in char_freq:
            char_freq[ch] = 1
        else:
            char_freq[ch] += 1
    
    count_keys = 0
    for key in char_freq.keys():
        count_keys += 1
    
    return count_keys

case1 = "aaabc"
print(minimizedStringLength(case1)) # 3

case2 = "cbbd"
print(minimizedStringLength(case2)) # 3

case3 = "dddaaa"
print(minimizedStringLength(case3)) # 2

case4 = "baadccab"
print(minimizedStringLength(case4)) # 4

case5 = "abcde"
print(minimizedStringLength(case5)) # 5