"""
Problem Description:
    - You are given a 0-indexed string word, consisting of lowercase English letters. You need to 
    select one index and remove the letter at that index from word so that the frequency of every 
    letter present in word is equal.
    - Return true if it is possible to remove one letter so that the frequency of all letters in 
    word are equal, and false otherwise.
    - Note:
        * The frequency of a letter x is the number of times it occurs in the string.
        * You must remove exactly one letter and cannot choose to do nothing.

Constraints:
    - 2 <= word.length <= 100
    - word consists of lowercase English letters only.
"""

from collections import Counter

def equalFrequency(word):
    """
    :type word: str
    :rtype: bool
    """
    letter_freq = Counter(word)

    for letter in list(letter_freq.keys()): #for all the letters that are part of word
        letter_freq[letter] -= 1    #simulate removing that letter once
        if letter_freq[letter] == 0:
            del letter_freq[letter]
        if len(set(letter_freq.values())) == 1: #if frequency of every letter are the same after removal of one letter
            return True
        
        letter_freq = Counter(word) #undo the changes
    
    return False

word = "abcc"
print(equalFrequency(word)) # Output: True

word2 = "aazz"
print(equalFrequency(word2)) # Output: False