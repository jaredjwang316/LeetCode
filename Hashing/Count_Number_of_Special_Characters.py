"""
Problem Description:
    - You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
    - Return the number of special letters in word.

Constraints:
    - 1 <= word.length <= 50
    - word consists of only lowercase and uppercase English letters.
"""

def numberOfSpecialChars(word):
    """
    :type word: str
    :rtype: int
    """
    special_mapping = dict()
    for i in range(26):
        special_mapping[chr(i + 97)] = False
    
    for ch in word:
        if ch.islower() == True:
            if ch.upper() in word:
                special_mapping[ch] = True
    
    count_special = 0
    for v in special_mapping.values():
        if v == True:
            count_special += 1
    
    return count_special

word = "aaAbcBC"
print("number of special characters:", numberOfSpecialChars(word))  # expected output: 3

word2 = "abc"
print("number of special characters:", numberOfSpecialChars(word2))  # expected output: 0

word3 = "abBCab"
print("number of special characters:", numberOfSpecialChars(word3))  # expected output: 1