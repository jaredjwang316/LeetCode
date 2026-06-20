"""
Problem Description:
    - You are given a string allowed consisting of distinct characters and an array of strings words. A string is 
    consistent if all characters in the string appear in the string allowed.  Return the number of consistent 
    strings in the array words.

Constraints:
    - 1 <= words.length <= 10^4
    - 1 <= allowed.length <= 26
    - 1 <= words[i].length <= 10
    - The characters in allowed are distinct.
    - words[i] and allowed contain only lowercase English letters.
"""

def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    allowed_letters = set(allowed)
    count = 0

    for word in words:
        flag = True
        for ch in word:
            if ch not in allowed_letters:
                flag = False
                break
        
        if flag == True:
            count += 1
    
    return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))   #2

allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed2, words2))   #7

allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed3, words3))   #4