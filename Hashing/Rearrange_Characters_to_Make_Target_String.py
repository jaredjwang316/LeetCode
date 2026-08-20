"""
Problem Description:
    - You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to 
    form new strings.
    - Return the maximum number of copies of target that can be formed by taking letters from s and 
    rearranging them.

Constraints:
    - 1 <= s.length <= 100
    - 1 <= target.length <= 10
    - s and target consist of lowercase English letters.
"""

from collections import Counter

def rearrangeCharacters(s, target):
    """
    :type s: str
    :type target: str
    :rtype: int
    """
    s_freq = Counter(s)
    target_freq = Counter(target)

    max_copies = float('inf')
    for k,v in target_freq.items():
        if k not in s_freq:
            return 0
        else:
            # The character with the fewest possible complete copies limits the number of target copies we can make
            max_copies = min(max_copies, s_freq[k] // v)
    
    return max_copies

s = "ilovecodingonleetcode"
target = "code"
print(rearrangeCharacters(s, target))  # Output: 2

s2 = "abcba"
target2 = "abc"
print(rearrangeCharacters(s2, target2))  # Output: 1

s3 = "abbaccaddaeea"
target3 = "aaaaa"
print(rearrangeCharacters(s3, target3))  # Output: 1