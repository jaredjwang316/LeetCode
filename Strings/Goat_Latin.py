# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 13:10:18 2025

@author: jwang

Problem Description:
    You are given a string sentence that consist of words separated by spaces. 
    Each word consists of lowercase and uppercase letters only.
    We would like to convert the sentence to "Goat Latin" (a made-up language) 
    The rules of Goat Latin are as follows:

        - If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append 
        "ma" to the end of the word.
            * For example, the word "apple" becomes "applema".
        - If a word begins with a consonant (i.e., not a vowel), remove the 
        first letter and append it to the end, then add "ma".
            * For example, the word "goat" becomes "oatgma".
        - Add one letter 'a' to the end of each word per its word index in the 
        sentence, starting with 1.
            * For example, the first word gets "a" added to the end, the second 
            word gets "aa" added to the end, and so on.

    Return the final sentence representing the conversion from sentence to Goat Latin.

Constraints:
    1 <= sentence.length <= 150
    sentence consists of English letters and spaces.
    sentence has no leading or trailing spaces.
    All the words in sentence are separated by a single space.

"""

def isVowel(c):
    if c in "AEIOUaeiou":
        return True
    return False

def toGoatLatin(sentence):
    """
    :type sentence: str
    :rtype: str
    """
    words = sentence.split(" ")
    final_sentence = ""
    for w in range(len(words)):
        if isVowel((words[w])[0]) == True:     #if word begins with a vowel
            words[w] += "ma"    #append ma to end of word
        else:
            words[w] = words[w] + (words[w])[0] + "ma"  #append first letter to the end, then add 'ma' to end of word
            words[w] = (words[w])[1:]   #remove the first letter

        for i in range(w + 1):
            words[w] += "a" #Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1
        final_sentence += words[w] + " "
    
    final_sentence = final_sentence[0:len(final_sentence) - 1]    #remove the last white space
    return final_sentence

sentence = "I speak Goat Latin"
print(toGoatLatin(sentence))

sentence2 = "The quick brown fox jumped over the lazy dog"
print(toGoatLatin(sentence2))