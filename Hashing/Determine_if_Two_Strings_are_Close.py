"""
Problem Description:
    - Two strings are considered close if you can attain one from the other using the following operations:
        - Operation 1: Swap any two existing characters.  
            - For example, abcde -> aecdb
        - Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
            - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    - You can use the operations on either string as many times as necessary.
    - Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Constraints:
    - 1 <= word1.length, word2.length <= 10^5
    - word1 and word2 contain only lowercase English letters.
"""

def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    if len(word1) != len(word2):
        return False
    
    word1_freq = dict()
    for ch in word1:
        if ch not in word2:
            return False
        if ch not in word1_freq:
            word1_freq[ch] = 1
        else:
            word1_freq[ch] += 1
    
    word2_freq= dict()
    for ch in word2:
        if ch not in word1:
            return False
        if ch not in word2_freq:
            word2_freq[ch] = 1
        else:
            word2_freq[ch] += 1
    
    freq_word1_list = []
    for val in word1_freq.values():
        freq_word1_list.append(val)
    freq_word1_list.sort()

    freq_word2_list = []
    for val in word2_freq.values():
        freq_word2_list.append(val)
    freq_word2_list.sort()

    if len(freq_word1_list) != len(freq_word2_list):
        return False
    
    for f in range(len(freq_word1_list)):
        if freq_word1_list[f] != freq_word2_list[f]:
            return False
    
    return True

word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))   # True

word3 = "a"
word4 = "aa"
print(closeStrings(word3, word4))   # False

word5 = "cabbba"
word6 = "abbccc"
print(closeStrings(word5, word6))   # True