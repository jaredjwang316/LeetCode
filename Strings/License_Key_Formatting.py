# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:20:10 2025

@author: jwang
"""
def licenseKeyFormatting(s, k):
    groups = []
    count_to_k = 0
    substring = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] != '-':
            if count_to_k < k:
                substring = s[i].upper() + substring
                count_to_k += 1
            else:
                groups.insert(0, substring)
                substring = str(s[i].upper())
                count_to_k = 1
    groups.insert(0, substring)

    reformatted_key = ""
    for g in groups:
        reformatted_key += g
        reformatted_key += "-"
    
    reformatted_key = reformatted_key[0:len(reformatted_key) - 1]   #remove the last dash since the last group should not be followed by a dash
    return reformatted_key

s = "5F3Z-2e-9-w"
k = 4

print(licenseKeyFormatting(s, k))

s1 = "2-5g-3-J"
k1 = 2
print(licenseKeyFormatting(s1, k1))

s2 = "12-5g-3-J"
k2 = 2
print(licenseKeyFormatting(s2, k2))

s3 = "412-5g-3-J"
k3 = 2
print(licenseKeyFormatting(s3, k3))