# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 23:23:52 2025

@author: jwang

Problem Description:
    For two strings s and t, we say "t divides s" if and only if s = t + t + t 
    + ... + t + t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x 
    divides both str1 and str2.

COnstraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

"""

def lengthGCD(len1, len2):
    if len1 < len2:
        temp = len1
        len1 = len2
        len2 = temp

    while(len2 != 0):
        temp = len1
        len1 = len2 
        len2 = temp % len2
    return len1

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if len(str2) > len(str1):
        temp = str2
        str2 = str1
        str1 = temp
    
    string_gcd = ""
    for i in range(len(str2)):
        str2_substring = str2[0:i + 1]

        if len(str1) % len(str2_substring) != 0 or len(str2) % len(str2_substring) != 0:    
            continue

        if str2_substring * (len(str2) // len(str2_substring)) != str2:
            continue

        concatenation = ""
        for i in range( len(str1) // len(str2_substring) ):
            concatenation += str2_substring

        if concatenation == str1:
            if len(str2_substring) > len(string_gcd):
                string_gcd = str2_substring

    if len(string_gcd) > lengthGCD(len(str1), len(str2)):
        return string_gcd[0:lengthGCD(len(str1), len(str2))]

    return string_gcd

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2)) #Ouput: "ABC"

str3 = "ABABAB"
str4 = "ABAB"
print(gcdOfStrings(str3, str4)) #Output: "AB"

str5 = "LEET"
str6 = "CODE"
print(gcdOfStrings(str5, str6)) #Output: ""
print(len(gcdOfStrings(str5, str6)))    #0

str7 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str8 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(gcdOfStrings(str7, str8)) #Output: "TAUXX"

str9 = "AAAAAAAAA"
str10 = "AAACCC"
print(gcdOfStrings(str9, str10)) #Output: ""
print(len(gcdOfStrings(str9, str10)))    #0