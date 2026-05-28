"""
Problem Description:
    - Given a string s of lower and upper case English letters.
    - A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
        - 0 <= i <= s.length - 2
        - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
    - To make the string good, you can choose two adjacent characters that make the string bad and 
    remove them. You can keep doing this until the string becomes good.
    - Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
    - Notice that an empty string is also good.

Constraints:
    - 1 <= s.length <= 100
    - s contains only lower and upper case English letters.
"""



def makeGood(s):
    """
    :type s: str
    :rtype: str
    """
    theStack = [s[0]]
    for i in range(1, len(s)):
        if len(theStack) > 0 and (theStack[-1]).isupper() == True and (theStack[-1]).lower() == s[i]:    #if s[i - 1] and s[i] is same letter but the former one is uppercase while the latter one is in lowercase
            theStack.pop()
        elif len(theStack) > 0 and s[i].isupper() == True and theStack[-1] == s[i].lower():   #if s[i - 1] and s[i] is the same letter but the former one is lowercase while the latter one is uppercase
            theStack.pop()
        else:
            theStack.append(s[i])
    
    return "".join(theStack)

s = "leEeetcode"
print(makeGood(s))  #Output: "leetcode"

s2 = "abBAcC"
print(makeGood(s2))  #Output: ""
if (makeGood(s2) == ""):
    print("The output is an empty string.")
    
s3 = "s"
print(makeGood(s3))  #Output: "s"
