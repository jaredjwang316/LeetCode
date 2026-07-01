"""
Problem Description:
    - You are given a string of length 5 called time, representing the current time on a digital clock 
    in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is 
    "23:59".
    - In the string time, the digits represented by the ? symbol are unknown, and must be replaced 
    with a digit from 0 to 9.
    - Return an integer answer, the number of valid clock times that can be created by replacing 
    every ? with a digit from 0 to 9.

Constraints:
    - time is a valid string of length 5 in the format "hh:mm".
    - "00" <= hh <= "23"
    - "00" <= mm <= "59"
    - Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
"""

def countTime(time):
    """
    :type time: str
    :rtype: int
    """
    time_components = time.split(":")
    
    permutations = 1
    
    if time_components[0] == "??":
        permutations = 24
    elif (time_components[0])[0] == "?":
        if (time_components[0])[1] > "3":
            permutations = 2    #can be 0 or 1
        else:
            permutations = 3    #can be 0, 1 or 2
    elif (time_components[0])[1] == "?":
        if (time_components[0])[0] < "2":
            permutations = 10   #can be any digit 
        else:
            permutations = 4    #can be 0, 1, 2 or 3
    
    if time_components[1] == "??":
        permutations *= 60  #there are 60 minutes in an hour
    elif (time_components[1])[0] == "?":
        permutations *= 6   #can be 0,1,2,3,4 or 5
    elif (time_components[1])[1] == "?":
        permutations *= 10  #can be any digit
    
    return permutations

time = "?5:00"
print(countTime(time))  # Output: 2

time2 = "0?:0?"
print(countTime(time2))  # Output: 100

time3 = "??:??"
print(countTime(time3))  # Output: 1440

time4 = "07:?3"
print(countTime(time4))  # Output: 6