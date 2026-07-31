"""
Problem Description:
    - You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
    - In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are 
    anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index 
    that satisfies the conditions.
    - Return words after performing all operations. It can be shown that selecting the indices for each 
    operation in any arbitrary order will lead to the same result.
    - An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all 
    the original letters exactly once. For example, "dacb" is an anagram of "abdc".

Constraints:
    - 1 <= words.length <= 100
    - 1 <= words[i].length <= 10
    - words[i] consists of lowercase English letters.
"""

def removeAnagrams(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    resultant_array = [words[0]]

    for i in range(1, len(words)):
        if "".join(sorted(words[i])) != "".join(sorted(resultant_array[-1])):
            resultant_array.append(words[i])
    
    return resultant_array

words = ["abba","baba","bbaa","cd","cd"]
print(removeAnagrams(words))  # Output: ['abba', 'cd']

words2 = ["a","b","c","d","e"]
print(removeAnagrams(words2))  # Output: ['a', 'b', 'c', 'd', 'e']