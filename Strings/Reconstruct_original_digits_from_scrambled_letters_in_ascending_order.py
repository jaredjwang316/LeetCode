# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:31:01 2025

@author: jwang
"""

def originalDigits(s):
    """
    :type s: str
    :rtype: str
    """
    
    count_zeros = s.count('z')
    count_twos = s.count('w')
    count_fours = s.count('u')
    count_sixs = s.count('x')
    count_eights = s.count('g')

    count_threes = s.count('h') - count_eights  #only 3 and 9 have the letter 'h' in english form and only 1 h
    count_fives = s.count('f') - count_fours    #only 4 and 5 have the letter 'f' in english form and only 1 f
    count_sevens = s.count('v') - count_fives   #only 5 and 7 have the letter 'v' in english form and only 1 v
    count_ones = s.count('o') - count_twos - count_fours - count_zeros    #only 0, 1, 2, and 4 have letter 'o' in english form and only 1 o
    count_nines = s.count('i') - count_fives - count_sixs - count_eights  #only 5, 6, 8, 9 have the letter 'n' in english form and only 1 i

    final_result = ""
    for a in range(count_zeros):
        final_result += "0"
    
    for b in range(count_ones):
        final_result += "1"
    
    for c in range(count_twos):
        final_result += "2"
    
    for d in range(count_threes):
        final_result += "3"

    for e in range(count_fours):
        final_result += "4"
    
    for f in range(count_fives):
        final_result += "5"

    for g in range(count_sixs):
        final_result += "6"
    
    for h in range(count_sevens):
        final_result += "7"

    for i in range(count_eights):
        final_result += "8"
    
    for j in range(count_nines):
        final_result += "9"
    
    return final_result


print(originalDigits("owoztneoer"))
print(originalDigits("fviefuro"))
print(originalDigits("nnei"))
print(originalDigits("xsi"))
