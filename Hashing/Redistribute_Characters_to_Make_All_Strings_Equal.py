"""
Problem Description:
    - You are given an array of strings words (0-indexed).
    - In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and 
    move any character from words[i] to any position in words[j].
    - Return true if you can make every string in words equal using any number of operations, and 
    false otherwise.

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 100
    - words[i] consists of lowercase English letters.
"""

def makeEqual(words):
    """
    :type words: List[str]
    :rtype: bool
    """
    char_freq = dict()

    for word in words:
        for ch in word:
            if ch not in char_freq:
                char_freq[ch] = 1
            else:
                char_freq[ch] += 1
    
    for v in char_freq.values():
        if v % len(words) != 0:
            return False
    
    return True

words = ["abc","aabc","bc"]
print(makeEqual(words))  # Output: True

words2 = ["ab","a"]
print(makeEqual(words2))  # Output: False

words3 = ["a","a","a"]
print(makeEqual(words3))  # Output: True

words4 = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
print(makeEqual(words4))  # Output: True

words5 = ["b"]
print(makeEqual(words5))  # Output: True

words6 = ["a", "b"]
print(makeEqual(words6))  # Output: False

