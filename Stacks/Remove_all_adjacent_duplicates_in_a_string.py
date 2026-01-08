"""
Problem Description:
    - You are given a string s consisting of lowercase English letters. A duplicate removal 
    consists of choosing two adjacent and equal letters and removing them.
    - We repeatedly make duplicate removals on s until we no longer can.
    - Return the final string after all such duplicate removals have been made. It can be 
    proven that the answer is unique.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
"""

def removeDuplicates(s):
    """
    :type s: str
    :rtype: str
    """
    letterStack = [s[0]]
    for ch in range(1, len(s)):
        if len(letterStack) > 0 and s[ch] == letterStack[-1]:
            letterStack.pop()
        else:
            letterStack.append(s[ch])
    
    result = ""
    for ch in letterStack:
        result += ch
    return result

print(removeDuplicates("abbaca")) #ca
print(removeDuplicates("azxxzy")) #ay
print(removeDuplicates("a")) #a