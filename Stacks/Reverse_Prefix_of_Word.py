"""
Problem Description:
    - Given a 0-indexed string word and a character ch, reverse the segment of word that starts at 
    index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does 
    not exist in word, do nothing.
    - For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts 
    at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
    - Return the resulting string.
"""

def reversePrefix(word, ch):
    """
    :type word: str
    :type ch: str
    :rtype: str
    """
    charStack = []
    index_cutoff = 0
    flag = False
    for i,letter in enumerate(word):
        charStack.append(letter)
        if letter == ch:
            index_cutoff = i
            flag = True
            break

    if flag == False:
        return word
        
    prefix_reverse = ""
    while len(charStack) > 0:
        prefix_reverse = prefix_reverse + charStack.pop()

    for i in range(index_cutoff + 1, len(word)):
        prefix_reverse += word[i]
    return prefix_reverse

word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))   # Output: "dcbaefd"

word2 = "xyxzxe"
ch2 = "z"
print(reversePrefix(word2, ch2))   # Output: "zxyxxe"

word3 = "abcd"
ch3 = "z"
print(reversePrefix(word3, ch3))   # Output: "abcd"