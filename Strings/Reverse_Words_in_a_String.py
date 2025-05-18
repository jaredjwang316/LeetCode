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
    s = s.lstrip()
    s = s.rstrip()
    
    consecutive_space_count = 0
    reversed_string = ""
    for i in range(len(s)):
        if s[i] != ' ':
            reversed_string += s[i]
            consecutive_space_count = 0
        else:
            consecutive_space_count += 1
            if consecutive_space_count > 1:
                continue
            reversed_string += s[i]
    
    word_extraction = reversed_string.split(" ")
    reverse_words = ""
    for w in range(len(word_extraction) - 1, -1, -1):
        reverse_words += word_extraction[w]
        if w > 0:
            reverse_words += " "
    return reverse_words     

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))