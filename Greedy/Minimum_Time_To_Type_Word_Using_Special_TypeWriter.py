"""
Problem Description:
    - There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with 
    a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is 
    initially pointing to the character 'a'.

Constraints:
    - 1 <= word.length <= 100
    - word consists of lowercase English letters. 
"""

def minTimeToType(word):
    """
    :type word: str
    :rtype: int
    """
    count_time = min(abs(ord(word[0]) - ord('a')), 26 - abs(ord(word[0]) - ord('a')))

    for i in range(1, len(word)):
        count_time += min(abs(ord(word[i]) - ord(word[i - 1])), 26 - abs(ord(word[i]) - ord(word[i - 1])))  #takes 26 seconds to move one full cycle around the circle
    
    return count_time + len(word)   #takes one second to type a character

word = "abc"
print(minTimeToType(word))  #Output: 5

word2 = "bza"
print(minTimeToType(word2))  #Output: 7

word3 = "zjpc"
print(minTimeToType(word3))  #Output: 34

