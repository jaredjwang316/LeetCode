"""
Problem Description:
    - You are given a string s that consists of lowercase English letters.
    - Return the string obtained by removing all trailing vowels from s.
    - The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.

Constraints:
    - 1 <= s.length <= 100
    - s consists of only lowercase English letters.
"""

def trimTrailingVowels(s):
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)

    while(len(s_list) > 0 and s_list[-1] in "aeiou"):
        s_list.pop()
    
    return "".join(s_list)

s = "idea"
print(trimTrailingVowels(s))  # Output: "id"

s2 = "day"
print(trimTrailingVowels(s2))  # Output: "day"

s3 = "aeiou"
if trimTrailingVowels(s3) == "":
    print("All vowels removed, output is an empty string.")  # Output: "All vowels removed, output is an empty string."