"""
Problem Description:
    - You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s 
    appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
    - Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
    - In a well-spaced string, the number of letters between the two occurrences of the ith letter is 
    distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.
    - Return true if s is a well-spaced string, otherwise return false.

Constraints:
    - 2 <= s.length <= 52
    - s consists only of lowercase English letters.
    - Each letter appears in s exactly twice.
    - distance.length == 26
    - 0 <= distance[i] <= 50
"""

def checkDistances(s, distance):
    """
    :type s: str
    :type distance: List[int]
    :rtype: bool
    """
    distance_dict = dict()
    unique_dict = dict()

    for i in range(26):
        distance_dict[chr(i + 97)] = distance[i]
    
    for i,ch in enumerate(s):
        if ch not in unique_dict:
            unique_dict[ch] = i
        else:
            if i - unique_dict[ch] - 1 != distance_dict[ch]:
                return False        


    return True

s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(checkDistances(s, distance))  # Output: True

s2 = "aa"
distance2 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(checkDistances(s2, distance2))  # Output: False