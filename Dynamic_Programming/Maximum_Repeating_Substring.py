"""
Problem Description:
    - For a string sequence, a string word is k-repeating if word concatenated k times is a substring of 
    sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in 
    sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.
    - Given strings sequence and word, return the maximum k-repeating value of word in sequence.     

Constraints:
    - 1 <= sequence.length <= 100
    - 1 <= word.length <= 100
    - sequence and word consist of lowercase English letters. 
"""

def maxRepeating(sequence, word):
    """
    :type sequence: str
    :type word: str
    :rtype: int
    """
    dp = []
    for i in range(len(sequence) + 1):
        dp.append(0)
    
    for i in range(len(word), len(sequence) + 1, 1):
        if sequence[i - len(word):i] == word:
            dp[i] = dp[i - len(word)] + 1
    
    return max(dp)

sequence = "ababc"
word = "ab"
print(maxRepeating(sequence, word))    #Expected output: 2

sequence2 = "ababc"
word2 = "ba"
print(maxRepeating(sequence2, word2))    #Expected output: 1

sequence3 = "ababc"
word3 = "ac"
print(maxRepeating(sequence3, word3))    #Expected output: 0

sequence4 = "a"
word4 = "a"
print(maxRepeating(sequence4, word4))    #Expected output: 1

sequence5 = "aaa"
word5 = "aa"
print(maxRepeating(sequence5, word5))    #Expected output: 1