"""
Problem Description:
    - You are given a string time in the form of  hh:mm, where some of the digits in the string 
    are hidden (represented by ?).  
    - The valid times are those inclusively between 00:00 and 23:59.
    - Return the latest valid time you can get from time by replacing the hidden digits.

Constraints:
    - time is in the format hh:mm.
    - It is guaranteed that you can produce a valid time from the given string.
"""

def maximumTime(time):
    """
    :type time: str
    :rtype: str
    """
    time_components = list(time)
    for t in range(len(time_components)):
        if time_components[t] == "?":
            if t == 0:
                if time_components[t + 1] != "?" and time_components[t + 1] >= "4":
                    time_components[t] = "1"
                else:
                    time_components[t] = "2"
            elif t == 1:
                if time_components[t - 1] == "2":
                    time_components[t] = "3"
                else:
                    time_components[t] = "9"
            elif t == 2:
                continue
            elif t == 3:
                time_components[t] = "5"
            else:
                time_components[t] = "9"
    
    return "".join(time_components)

time = "2?:?0"
print(maximumTime(time))    # Output: "23:50"

time2 = "0?:3?"
print(maximumTime(time2))   # Output: "09:39"

time3 = "1?:22"
print(maximumTime(time3))   # Output: "19:22"

time4 = "?4:03"
print(maximumTime(time4))   # Output: "14:03"

time5 = "??:??"
print(maximumTime(time5))   # Output: "23:59"