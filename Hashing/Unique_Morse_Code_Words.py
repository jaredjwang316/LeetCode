# -*- coding: utf-8 -*-
"""
Created on Tue May 20 17:45:48 2025

@author: jwang
"""

def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """

    #dictionary converts english letters into unique morse code words
    morseDict = {
        'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
        'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 
        's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
    }

    transformations = []
    for w in range(len(words)):
        morseCode = ""
        for ch in words[w]:
            morseCode += morseDict[ch]
        
        if morseCode not in transformations:
            transformations.append(morseCode)
    
    return len(transformations)

words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))