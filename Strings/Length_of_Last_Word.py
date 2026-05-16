"""
Problem Description:
    - Given a string s consisting of words and spaces, return the length of the last word in the string.
    - A word is a maximal substring consisting of non-space characters only.

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of only English letters and spaces ' '.
    - There will be at least one word in s.
"""

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    last_index = len(s) - 1
    while(last_index >= 0):
        if s[last_index] == ' ':
            last_index -= 1
        else:
            break
    
    last_word = ""
    for i in range(last_index, -1, -1):
        if s[i] == ' ':
            break
        else:
            last_word = s[i] + last_word
    
    return len(last_word)

s = "Hello World"
print(lengthOfLastWord(s)) # Output: 5

s2 = "   fly me   to   the moon  "
print(lengthOfLastWord(s2)) # Output: 4

s3 = "luffy is still joyboy"
print(lengthOfLastWord(s3)) # Output: 6

s4 = "            "
print(lengthOfLastWord(s4)) # Output: 0