# -*- coding: utf-8 -*-
"""
Created on Sat May 31 16:39:43 2025

@author: jwang
"""

def findPoisonedDuration(timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    poison_time = duration  #the first attack, Ashe gets poisoned for the duration time
    for t in range(1, len(timeSeries)): #overlapping in time from the previous poison attack
        if timeSeries[t] == timeSeries[t - 1]:
            continue
        if timeSeries[t] > timeSeries[t - 1] and timeSeries[t] < (timeSeries[t - 1] + duration):
            poison_time += (timeSeries[t] - timeSeries[t - 1])
        else:
            poison_time += duration
        

    return poison_time

timeSeries = [1,4]
duration = 2
print(findPoisonedDuration(timeSeries, duration))

timeSeries2 = [1,2]
duration2 = 2
print(findPoisonedDuration(timeSeries2, duration2))

timeSeries3 = [1,2,3,4,5]
duration3 = 5
print(findPoisonedDuration(timeSeries3, duration3))

timeSeries4 = [7,12,12]
duration4 = 5
print(findPoisonedDuration(timeSeries4, duration4))
