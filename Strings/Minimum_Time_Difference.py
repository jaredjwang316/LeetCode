# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 22:00:57 2025

@author: jwang

Problem Description:
    Given a list of 24-hour clock time points in "HH:MM" format, return the 
    minimum minutes difference between any two time-points in the list. 
    
Constraints:
    2 <= timePoints.length <= 2 * 104
    timePoints[i] is in the format "HH:MM".
"""

def convertToMinutes(time):
    time_parts = time.split(":")
    return 60 * int(time_parts[0]) + int(time_parts[1])

def findMinDifference(timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """

    minutes_list = []
    for time in timePoints:
        minutes_list.append(convertToMinutes(time))
    minutes_list.sort()

    min_diff = 1440
    for i in range(1, len(minutes_list)):
        if minutes_list[i] - minutes_list[i - 1] < min_diff:
            min_diff = minutes_list[i] - minutes_list[i - 1]

    min_diff = min(min_diff, 1440 - minutes_list[-1] + minutes_list[0]) #need to consider the difference between the last time of that day to the first time of the next day
    return min_diff

timePoints = ["23:59","00:00"]
print(findMinDifference(timePoints))    #1

timePoints2 = ["00:00","23:59","00:00"]
print(findMinDifference(timePoints2))   #0

timePoints3 = ["02:39","10:26","21:43"]
print(findMinDifference(timePoints3))   #296

timePoints4 = ["00:00","23:59"]
print(findMinDifference(timePoints4))   #1