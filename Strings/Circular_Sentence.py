"""
Problem Description:
    - A sentence is a list of words that are separated by a single space with no leading or trailing 
    spaces.
        * For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
    - Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English 
    letters are considered different.
    - A sentence is circular if:
        * The last character of each word in the sentence is equal to the first character of its next word.
        * The last character of the last word is equal to the first character of the first word.
    - For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all 
    circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" 
    are not circular sentences.
    - Given a string sentence, return true if it is circular. Otherwise, return false.

Constraints:
    - 1 <= sentence.length <= 500
    - sentence consist of only lowercase and uppercase English letters and spaces.
    - The words in sentence are separated by a single space.
    - There are no leading or trailing spaces.
"""

def isCircularSentence(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    words = sentence.split(" ")
    
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]: #if the first character of current word is not equal to last character of its left word
            return False
    
    if words[-1][-1] != words[0][0]:    #if the last character of the last word is not equal to the first character of the first word
        return False

    return True

sentence = "leetcode exercises sound delightful"
print(isCircularSentence(sentence))  # Output: True

sentence2 = "eetcode"
print(isCircularSentence(sentence2))  # Output: True

sentence3 = "Leetcode is cool"
print(isCircularSentence(sentence3))  # Output: False

sentence4 = "leetcode"
print(isCircularSentence(sentence4))  # Output: False

sentence5 = "Leetcode eisc cool"
print(isCircularSentence(sentence5))  # Output: False