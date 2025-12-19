"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    pairing = dict()

    for i in range(len(s)):
        if s[i] not in pairing:
            pairing[s[i]] = t[i]
        else:
            if t[i] != pairing[s[i]]:
                return False
    
    pairing2 = dict()
    for i in range(len(t)):
        if t[i] not in pairing2:
            pairing2[t[i]] = s[i]
        else:
            if s[i] != pairing2[t[i]]:
                return False
    return True

s = "egg"
t = "add"
print(isIsomorphic(s, t))  # Output: True

s2 = "foo"
t2 = "bar"
print(isIsomorphic(s2, t2))  # Output: False

s3 = "paper"
t3 = "title"    
print(isIsomorphic(s3, t3))  # Output: True

s4 = "badc"
t4 = "baba"
print(isIsomorphic(s4, t4))  # Output: False