"""
Problem Description:
    - Given a sentence that consists of some words separated by a single space, and a 
    searchWord, check if searchWord is a prefix of any word in sentence.

    - Return the index of the word in sentence (1-indexed) where searchWord is a 
    prefix of this word. If searchWord is a prefix of more than one word, return 
    the index of the first word (minimum index). If there is no such word return -1.

    - A prefix of a string s is any leading contiguous substring of s.

Constraints:
    - 1 <= sentence.length <= 100
    - 1 <= searchWord.length <= 10
    - sentence consists of lowercase English letters and spaces.
    - searchWord consists of lowercase English letters.
"""

def isPrefixOfWord(sentence, searchWord):
    """
    :type sentence: str
    :type searchWord: str
    :rtype: int
    """
    words = sentence.split(" ")

    for i, word in enumerate(words):
        if len(word) < len(searchWord):
            continue
        if word[0:len(searchWord)] == searchWord:
            return i + 1
    return -1

sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence, searchWord)) # Output: 4

sentence2 = "this problem is an easy problem"
searchWord2 = "pro"
print(isPrefixOfWord(sentence2, searchWord2)) # Output: 2

sentence3 = "hellohello hellohellohello"
searchWord3 = "ell"
print(isPrefixOfWord(sentence3, searchWord3)) # Output: -1