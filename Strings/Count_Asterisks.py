"""
Problem Description:
    - You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In 
    other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
    - Return the number of '*' in s, excluding the '*' between each pair of '|'.
    - Note that each '|' will belong to exactly one pair.

Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
    - s contains an even number of vertical bars '|'.
"""

def countAsterisks(s):
    """
    :type s: str
    :rtype: int
    """
    filtered_string = ""
    count_pipes = 0

    for ch in s:
        if ch == "|":
            count_pipes += 1
            continue
        if count_pipes % 2 == 0:    #excluding the characters that are between each pair of | occurs when the number of pipes we have visited is odd
            filtered_string += ch
    
    count_asterisk = 0
    for ch in filtered_string:
        if ch == "*":
            count_asterisk += 1
    
    return count_asterisk

s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))    #Output: 2

s2 = "iamprogrammer"
print(countAsterisks(s2))    #Output: 0

s3 = "yo|uar|e**|b|e***au|tifu|l"
print(countAsterisks(s3))    #Output: 5