"""
Problem Description:
    - You are given two strings current and correct representing two 24-hour times.  24-hour times 
    are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The 
    earliest 24-hour time is 00:00, and the latest is 23:59.
    - In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform 
    this operation any number of times.
    - Return the minimum number of operations needed to convert current to correct.

Constraints:
    - current and correct are in the format "HH:MM"
    - current <= correct
"""

def convertTime(current, correct):
    """
    :type current: str
    :type correct: str
    :rtype: int
    """
    current_time_components = current.split(":")
    correct_time_components = correct.split(":")

    hour_diff = 0   #see how many hours, or 60 minutes can fully fit in the time difference first
    minute_diff = 0
    if current_time_components[1] <= correct_time_components[1]:
        minute_diff = max( int(correct_time_components[1]), int(current_time_components[1]) ) - min( int(correct_time_components[1]), int(current_time_components[1]) )
        hour_diff = int(correct_time_components[0]) - int(current_time_components[0])
    else:
        minute_diff = 60 - (max ( int(correct_time_components[1]), int(current_time_components[1]) ) - min( int(correct_time_components[1]), int(current_time_components[1]) ) )
        hour_diff = int(correct_time_components[0]) - int(current_time_components[0]) - 1
    
    fit_15_minutes = minute_diff // 15  #first find how many 15 minutes can perfectly fit in 
    minute_diff = minute_diff - 15 * fit_15_minutes
    fit_5_minutes = minute_diff // 5    #then see how many 5 minutes can perfectly fit in

    return hour_diff + fit_15_minutes + fit_5_minutes + (minute_diff % 5)   #minute_dff % 5 represents how much 1 minutes can fit in

current = "02:30"
correct = "04:35"
print(convertTime(current, correct))    #Output: 3

current2 = "11:00"
correct2 = "11:01"
print(convertTime(current2, correct2))  #Output: 1

current3 = "00:00"
correct3 = "00:00"
print(convertTime(current3, correct3))  #Output: 0

current4 = "09:41"
correct4 = "10:34"
print(convertTime(current4, correct4))  #Output: 7

current5 = "03:48"
correct5 = "04:16"
print(convertTime(current5, correct5))  #Output: 6

