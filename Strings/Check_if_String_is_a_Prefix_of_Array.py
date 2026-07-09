"""
Problem Description:
    - Given a string s and an array of strings words, determine whether s is a prefix string of words.
    - A string s is a prefix string of words if s can be made by concatenating the first k strings in 
    words for some positive k no larger than words.length.
    - Return true if s is a prefix string of words, or false otherwise.

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 20
    - 1 <= s.length <= 1000
    - words[i] and s consist of only lowercase English letters.
"""

def isPrefixString(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: bool
    """
    combined_word = ""
    for word in words:
        combined_word += word

        if len(combined_word) > len(s):
            return False
        elif combined_word == s:
            return True
    
    return False

s = "iloveleetcode"
word = ["i","love","leetcode","apples"]
print(isPrefixString(s, word))  # Output: True

s2 = "iloveleetcode"
word2 = ["apples","i","love","leetcode"]
print(isPrefixString(s2, word2))  # Output: False