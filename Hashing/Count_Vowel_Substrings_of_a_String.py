"""
Problem Description:
    - A substring is a contiguous (non-empty) sequence of characters within a string.
    - A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and 
    has all five vowels present in it.
    - Given a string word, return the number of vowel substrings in word.

Constraints:
    - 1 <= word.length <= 100
    - word consists of lowercase English letters only.
"""

def isVowel(letter):
    if letter in "aeiou":
        return True
    return False

def countVowelSubstrings(word):
    """
    :type word: str
    :rtype: int
    """
    vowel_set = set()
    count_vowel_substring = 0

    for i in range(len(word) - 1):
        if isVowel(word[i]) == True:
            vowel_set.add(word[i])
        else:
            vowel_set = set()
            continue

        for j in range(i + 1, len(word)):
            if isVowel(word[j]) == True:
                vowel_set.add(word[j])

                if len(vowel_set) == 5:
                    count_vowel_substring += 1
            else:
                vowel_set = set()
                break

        vowel_set = set()

    return count_vowel_substring 

word = "aeiouu"
print(countVowelSubstrings(word))  # Output: 2

word2 = "unicornarihan"
print(countVowelSubstrings(word2))  # Output: 0

word3 = "cuaieuouac"
print(countVowelSubstrings(word3))  # Output: 7

word4 = "poazaeuioauoiioaouuouaui"
print(countVowelSubstrings(word4))  # Output: 31