"""
Problem Description:
    - Two strings word1 and word2 are considered almost equivalent if the differences between the 
    frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
    - Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost 
    equivalent, or false otherwise.  The frequency of a letter x is the number of times it occurs 
    in the string.

Constraints:
    - n == word1.length == word2.length
    - 1 <= n <= 100
    - word1 and word2 consist only of lowercase English letters.
"""

from collections import Counter

def checkAlmostEquivalent(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    word1_freq = Counter(word1)
    word2_freq = Counter(word2)

    for k,v in word1_freq.items():
        if k in word2_freq:
            if abs(v - word2_freq[k]) > 3:
                return False
        else:
            if v > 3:
                return False
    
    for k,v in word2_freq.items():
        if k not in word1_freq:
            if v > 3:
                return False
    
    return True

word1 = "aaaa"
word2 = "bccb"
print(checkAlmostEquivalent(word1, word2))  #False

word3 = "abcdeef"
word4 = "abaaacc"
print(checkAlmostEquivalent(word3, word4))  #True

word5 = "cccddabba"
word6 = "babababab"
print(checkAlmostEquivalent(word5, word6))  #True