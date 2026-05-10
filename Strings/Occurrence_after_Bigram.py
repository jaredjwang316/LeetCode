"""
Problem Description:
    - Given two strings first and second, consider occurrences in some text of the form "first second third", 
    where second comes immediately after first, and third comes immediately after second.
    - Return an array of all the words third for each occurrence of "first second third".

Constraints:
    - 1 <= text.length <= 1000
    - text consists of lowercase English letters and spaces.
    - All the words in text are separated by a single space.
    - 1 <= first.length, second.length <= 10
    - first and second consist of lowercase English letters.
    - text will not have any leading or trailing spaces.
"""

def findOcurrences(text, first, second):
    """
    :type text: str
    :type first: str
    :type second: str
    :rtype: List[str]
    """
    words = text.split(" ")

    afterBigram = []
    for w in range(1, len(words)):
        if words[w] == second and words[w - 1] == first:
            if w != len(words) - 1:
                afterBigram.append(words[w + 1])

    return afterBigram

text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(findOcurrences(text, first, second))   #["girl","student"]

text2 = "we will we will rock you"
first2 = "we"
second2 = "will"
print(findOcurrences(text2, first2, second2))   #["we","rock"]

text3 = "we we we we will rock you"
first3 = "we"
second3 = "we"
print(findOcurrences(text3, first3, second3))   #["we","we","will"]


