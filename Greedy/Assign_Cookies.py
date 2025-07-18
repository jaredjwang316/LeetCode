# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 21:50:24 2025

@author: jwang

Problem Description:
    Assume you are an awesome parent and want to give your children some cookies. 
    But, you should give each child at most one cookie.

    Each child i has a greed factor g[i], which is the minimum size of a cookie 
    that the child will be content with; and each cookie j has a size s[j]. 
    If s[j] >= g[i], we can assign the cookie j to the child i, and the child i 
    will be content. Your goal is to maximize the number of your content children 
    and output the maximum number.

Constraints:
    
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1
"""

def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g.sort()
    s.sort()

    i = 0
    j = 0

    while(i < len(g) and j < len(s)):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i

g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))    #1

g2 = [1,2]
s2 = [1,2,3]
print(findContentChildren(g2, s2))  #2

g3 = [10,9,8,7]
s3 = [10,9,8,7]
print(findContentChildren(g3, s3))  #4

g4 = [1,2,3]
s4 = [3]
print(findContentChildren(g4, s4))  #1