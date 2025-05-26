# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:34:35 2025

@author: jwang
"""

def camelMatch(queries, pattern):
    """
    :type queries: List[str]
    :type pattern: str
    :rtype: List[bool]
    """
    ccm = []
    for q in queries:
        x = 0
        y = 0
        flag = True
        while(x < len(q) and y < len(pattern)):
            if q[x] == pattern[y]:
                y += 1
            else:
                if q[x].islower() == False:
                    flag = False
            x += 1 
        
        while(x < len(q)):
            if q[x].islower() == False:
                flag = False                
            x += 1
        
        if flag:
            if y == len(pattern):
                ccm.append(True)
            else:
                ccm.append(False)
        else:
            ccm.append(False)
    
    return ccm

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
print(camelMatch(queries, pattern))

queries1 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern1 = "FoBa"
print(camelMatch(queries1, pattern1))

queries2 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern2 = "FoBaT"
print(camelMatch(queries2, pattern2))