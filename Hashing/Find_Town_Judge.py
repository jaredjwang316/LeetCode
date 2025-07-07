# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 19:22:44 2025

@author: jwang

Problem Description:
    In a town, there are n people labeled from 1 to n. There is a rumor that 
    one of these people is secretly the town judge.
    
    If the town judge exists, then:
        - The town judge trusts nobody.
        - Everybody (except for the town judge) trusts the town judge.
        - There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the 
    person labeled ai trusts the person labeled bi. If a trust relationship does 
    not exist in trust array, then such a trust relationship does not exist.
    
    Return the label of the town judge if the town judge exists and can be 
    identified, or return -1 otherwise.

Constraints:
    
    1 <= n <= 1000
    0 <= trust.length <= 10^4
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
"""

def findJudge(n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    if len(trust) == 0: #edge case
        if n == 1:
            return n
        else:
            return -1
    
    trust_freq = dict() #keep track of the people who trusts that possible town judge
    notJudges = []  #list of the labels that we can quickly eliminate, meaning they cannot be judges
    for t in trust:
        if t[1] not in trust_freq:
            trust_freq[t[1]] = [t[0]]
        else:
            trust_freq[t[1]].append(t[0])
        notJudges.append(t[0])  #a judge cannot trust anyone
    
    

    for k,v in trust_freq.items():
        if len(v) == n - 1 and k not in notJudges:  #everybody (except the judge himself) trusts the town judge
            return k

    return -1

n = 2
trust = [[1,2]]
print(findJudge(n, trust))  #2

n2 = 3 
trust2 = [[1,3],[2,3]]
print(findJudge(n2, trust2))    #3

n3 = 3
trust3 = [[1,3],[2,3],[3,1]]
print(findJudge(n3, trust3))    #-1

n4 = 4
trust4 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(findJudge(n4, trust4))    #3

n5 = 4
trust5 = [[1,3],[1,4],[2,3]]
print(findJudge(n5, trust5))    #-1



