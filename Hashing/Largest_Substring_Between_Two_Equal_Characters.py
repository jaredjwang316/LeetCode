"""
Problem Description:
    - Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If 
    there is no such substring return -1.
    - A substring is a contiguous sequence of characters within a string.

Constraints:
    - <= s.length <= 300
    - s contains only lowercase English letters.
"""

def maxLengthBetweenEqualCharacters(s):
    """
    :type s: str
    :rtype: int
    """
    
    first_char_occurrence = dict()
    largest_substring = -1

    for i,ch in enumerate(s):
        if ch not in first_char_occurrence:
            first_char_occurrence[ch] = i
        else:
            largest_substring = max(largest_substring, i - first_char_occurrence[ch] - 1)   #exclude the two characters that are equal
    
    return largest_substring

s = "aa"
print(maxLengthBetweenEqualCharacters(s))  # Output: 0

s2 = "abca"
print(maxLengthBetweenEqualCharacters(s2))  # Output: 2

s3 = "cbzxy"
print(maxLengthBetweenEqualCharacters(s3))  # Output: -1