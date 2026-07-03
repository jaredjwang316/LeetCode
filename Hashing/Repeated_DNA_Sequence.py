# -*- coding: utf-8 -*-
"""
Problem Description:
    - The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
        * For example, "ACGAATTCCG" is a DNA sequence.
    - When studying DNA, it is useful to identify repeated sequences within the DNA.
    - Given a string s that represents a DNA sequence, return all the 10-letter-long sequences 
    (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is either 'A', 'C', 'G', or 'T'.
"""

def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    unique_dna = set()
    repeated_dna = set()

    for i in range(len(s) - 9):
        if s[i:i + 10] not in unique_dna:
            unique_dna.add(s[i:i + 10])
        else:
            repeated_dna.add(s[i:i + 10])
    
    return list(repeated_dna)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) #Output: ["AAAAACCCCC","CCCCCAAAAA"]
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))    #Output: ["AAAAAAAAAA"]
