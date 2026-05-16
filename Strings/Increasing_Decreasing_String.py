"""
Problem Description:
    - You are given a string s. Reorder the string using the following algorithm:
        - Remove the smallest character from s and append it to the result.
        - Remove the smallest character from s that is greater than the last appended character, and append it to the result.
        - Repeat step 2 until no more characters can be removed.
        - Remove the largest character from s and append it to the result.
        - Remove the largest character from s that is smaller than the last appended character, and append it to the result.
        - Repeat step 5 until no more characters can be removed.
        - Repeat steps 1 through 6 until all characters from s have been removed.

    - If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
    - Return the resulting string after reordering s using this algorithm.

Constraints:
    - 1 <= s.length <= 500
    - s consists of only lowercase English letters.
"""

def sortString(s):
    """
    :type s: str
    :rtype: str
    """

    result = ""
    s_list = list(s)
    while len(s_list) > 0:
        for ch in sorted(set(s_list)):
            result += ch
            s_list.remove(ch)
        
        for ch in sorted(set(s_list), reverse = True):
            result += ch
            s_list.remove(ch)
    
    return result

s = "aaaabbbbcccc"
print(sortString(s)) # Output: "abccbaabccba"

s2 = "rat"
print(sortString(s2)) # Output: "art"

