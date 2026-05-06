"""
Problem Description:
    You are given a 0-indexed string array words having length n and containing 0-indexed strings.
    You are allowed to perform the following operation any number of times (including zero):
        - Choose integers i, j, x, and y such that 0 <= i, j < n, 0 <= x < words[i].length, 0 <= y < words[j].length, 
        and swap the characters words[i][x] and words[j][y].
    Return an integer denoting the maximum number of words can contain, after performing some operations.
    Note: i and j may be equal during an operation.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.
"""

def maxPalindromesAfterOperations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    letter_freq = dict()
    for word in words:
        for ch in word:
            if ch not in letter_freq:
                letter_freq[ch] = 1
            else:
                letter_freq[ch] += 1
    
    count_pairs = 0
    # A palindrome needs pairs of identical characters for symmetric positions.
    for val in letter_freq.values():
        count_pairs = count_pairs + (val // 2)
    
    # Greedy step: Sort words by length so we try to build palindromes for the cheapest words first.
    # Smaller words require fewer pairs.  This helps maximize the total number of palindromes.
    words.sort(key = len)   

    max_palindromes = 0
    for word in words:
        need = len(word) // 2   #Cost of making this word a palindrome: Each pair fills two mirrored positions.
        if count_pairs >= need:     # If we have enough pairs, we can "pay" for this palindrome
            count_pairs -= need     # spend pairs (resource consumption)
            max_palindromes += 1    # successfully form one palindrome
        else:
            break   # Since words are sorted by length, if we can't afford this, we can't afford any further words.

    return max_palindromes

words = ["abbb","ba","aa"]
print(maxPalindromesAfterOperations(words))  # Output: 3

words2 = ["abc","ab"]
print(maxPalindromesAfterOperations(words2))  # Output: 2

words3 = ["cd","ef","a"]
print(maxPalindromesAfterOperations(words3))  # Output: 1

words4 = ["cd","ef","ag"]
print(maxPalindromesAfterOperations(words4))  # Output: 0