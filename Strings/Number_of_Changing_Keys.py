"""
Problem Description:
    - You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key 
    different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" 
    does not have any.
    - Return the number of times the user had to change the key.
    - Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user 
    typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.

Constraints:
    - 1 <= s.length <= 100
    - s consists of only upper case and lower case English letters
"""

def countKeyChanges(s):
    """
    :type s: str
    :rtype: int
    """
    count_change = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i - 1].lower():
            count_change += 1
    
    return count_change

s = "aAbBcC"
print(countKeyChanges(s))  # Output: 2

s2 = "AaAaAaaA"
print(countKeyChanges(s2))  # Output: 0