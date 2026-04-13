# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:41:21 2025

@author: jwang
"""

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s_words = s.split(" ")
    i = 0
    while(i < len(s_words)):    #remove leading and trailing whitesapces in a string
        if s_words[i] == '':
            s_words.pop(i)
        else:
            i += 1
    
    left = 0
    right = len(s_words) - 1

    while(left <= right):   #reverse the words
        temp = s_words[left]
        s_words[left] = s_words[right]
        s_words[right] = temp

        left += 1
        right -= 1
    
    result = ""
    for i in range(len(s_words)):
        if i != len(s_words) - 1:
            result = result + s_words[i] + " "
        else:
            result += s_words[i]
    return result   

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))