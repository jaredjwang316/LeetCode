"""
Problem Description:
    - Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
    space-separated sequence of one or more dictionary words.
    - Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:
    - 1 <= s.length <= 300
    - 1 <= wordDict.length <= 1000
    - 1 <= wordDict[i].length <= 20
    - s and wordDict[i] consist of only lowercase English letters.
    - All the strings of wordDict are unique.
"""

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    wordSet = set(wordDict)

    dp = []
    for i in range(len(s) + 1):
        dp.append(False)
    dp[0] = True    #Empty string is segmentable
    
    for i in range(1, len(dp), 1):
        for j in range(0, i, 1):
            if dp[j] == True and s[j:i] in wordSet: #if an already valid prefix can be further augmented/segmented into the available words
                dp[i] = True
    
    return dp[-1]   #determines if s can be segmented into the words available in wordDict

s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict)) #Output: True

s2 = "applepenapple"
wordDict2 = ["apple", "pen"]
print(wordBreak(s2, wordDict2)) #Output: True

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s3, wordDict3)) #Output: False

s4 = "cars"
wordDict4 = ["car","ca","rs"]
print(wordBreak(s4, wordDict4)) #Output: True

s5 = "aaaaaaa"
wordDict5 = ["aaaa","aaa"]
print(wordBreak(s5, wordDict5)) #Output: True

s6 = "a"
wordDict6 = ["aa","aaa","aaaa","aaaaa","aaaaaa"]
print(wordBreak(s6, wordDict6)) #Output: False