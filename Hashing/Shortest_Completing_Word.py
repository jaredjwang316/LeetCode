"""
Problem Description:
    Given a string licensePlate and an array of strings words, find the shortest completing word in words.

    A completing word is a word that contains all the letters in licensePlate. Ignore numbers and 
    spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in 
    licensePlate, then it must appear in the word the same number of times or more.

    For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' 
    twice. Possible completing words are "abccdef", "caaacab", and "cbca".

    Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple 
    shortest completing words, return the first one that occurs in words.

Constraints:
    1 <= licensePlate.length <= 7
    licensePlate consists of digits, letters (uppercase or lowercase), or space ' '.
    1 <= words.length <= 1000
    1 <= words[i].length <= 15
    words[i] consists of lowercase letters.
"""

def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    letter_freq = dict()

    for ch in licensePlate:
        if ch.isalpha() == True:    #ignore numbers and spaces, considering only letters
            if ch.lower() not in letter_freq:   #case insensitive
                letter_freq[ch.lower()] = 1
            else:
                letter_freq[ch.lower()] += 1
    
    comparables = []

    for word in words:
        subDict = dict()
        for ch in word:
            if ch in letter_freq:
                if ch not in subDict:
                    subDict[ch] = 1
                else:
                    subDict[ch] += 1
        
        flag = True
        for k,v in subDict.items():
            if v < letter_freq[k]:  #If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
                flag = False
        
        if len(subDict) != len(letter_freq):    #case: not all letters that are part of licensePlate were included in word
            flag = False

        if flag == True:
            comparables.append(word)

    shortest_length = len(comparables[0])
    for w in range(1, len(comparables)):
        if len(comparables[w]) < shortest_length:
            shortest_length = len(comparables[w])

    for c in comparables:
        if len(c) == shortest_length:
            return c 
    return ""

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
print(shortestCompletingWord(licensePlate, words))  # Output: "steps"

licensePlate2 = "1s3 456"
words2 = ["looks","pest","stew","show"]
print(shortestCompletingWord(licensePlate2, words2))  # Output: "pest"

licensePlate3 = "Ah71752"
words3 = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
print(shortestCompletingWord(licensePlate3, words3))  # Output: "husband"