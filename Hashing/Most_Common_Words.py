"""
Problem Description:
    - Given a string paragraph and a string array of the banned words banned, return the most frequent 
    word that is not banned. It is guaranteed there is at least one word that is not banned, and that 
    the answer is unique.
    - The words in paragraph are case-insensitive and the answer should be returned in lowercase.
    - Note that words can not contain punctuation symbols.

Constraints:
    - 1 <= paragraph.length <= 1000
    - paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
    - 0 <= banned.length <= 100
    - 1 <= banned[i].length <= 10
    - banned[i] consists of only lowercase English letters.
"""

def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    filter_punctuations = ""
    for ch in paragraph:
        if ch not in "!?',;.":  #word cannot contain punctuation symbols
            filter_punctuations += ch
        else:
            filter_punctuations += " "  #possiblity when letters are separated by only punctuations without spaces in them

    words = filter_punctuations.split(" ")
    i = 0
    while(i < len(words)):
        if words[i] == '':
            words.remove('')
        else:
            i += 1

    for w in range(len(words)):
        words[w] = (words[w]).lower()
    
    most_frequent_word = ""

    word_freq = dict()
    for word in words:
        if word in banned:
            continue
        else:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    
    max_freq = 0
    for k,v in word_freq.items():
        if v > max_freq:
            max_freq = v
            most_frequent_word = k
        
    return most_frequent_word

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))    #Output: "ball"

paragraph2 = "a."
banned2 = []
print(mostCommonWord(paragraph2, banned2))    #Output: "a"

paragraph3 = "a b.b"
banned3 = []
print(mostCommonWord(paragraph3, banned3))    #Output: "b"