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
    store_words = s.split(" ")
    s_words = []
    for word in store_words:
        if word != '':
            s_words.append(word)
    
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