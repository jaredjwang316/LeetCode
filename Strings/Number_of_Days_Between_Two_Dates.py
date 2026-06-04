"""
Problem Description:
    - Write a program to count the number of days between two dates.
    - The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
"""

def isLeapYear(year):
    if year % 100 == 0 and year % 400 != 0: #year 2000 is a leap year while year 1900 is not a leap year
        return False
    if year % 4 != 0:
        return False
    return True

def daysBetweenDates(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    if date1 > date2:
        temp = date1
        date1 = date2
        date2 = temp

    date1_components = date1.split("-")
    date2_components = date2.split("-")

    count_days = 0
    #count full years that passes between the two dates
    for yr in range(int(date1_components[0]) + 1, int(date2_components[0]), 1):
        if isLeapYear(yr) == True:
            count_days += 366
        else:
            count_days += 365
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(int(date1_components[0])) == True:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    
    #count the days in the full months of that passes in that year
    if date1_components[0] != date2_components[0]:
        for month in range(int(date1_components[1]) + 1, 13, 1):
            count_days += days_in_month[month - 1]

    if isLeapYear(int(date2_components[0])) == True:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    
    #count the days in the full months that completely passes in that year
    if date1_components[0] != date2_components[0]:
        for month in range(1, int(date2_components[1]), 1):
            count_days += days_in_month[month - 1]

    #count the days that passes the incomplete months
    if date1_components[0] != date2_components[0] or date1_components[1] != date2_components[1]:    #different year and/or month
        if isLeapYear(int(date1_components[0])) == True:
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        count_days = count_days + (days_in_month[int(date1_components[1]) - 1] - int(date1_components[2]))
        if isLeapYear(int(date2_components[0])) == True:
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        count_days = count_days + int(date2_components[2]) 
    else: #same year and month
        count_days = count_days + int(date2_components[2]) - int(date1_components[2])
    
    return count_days

date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))   #Output: 1

date3 = "2020-01-15"
date4 = "2019-12-31"
print(daysBetweenDates(date3, date4))   #Output: 15

date5 = "1971-06-29"
date6 = "2010-09-23"
print(daysBetweenDates(date5, date6))   #Output: 14331

date7 = "2086-02-28"
date8 = "1972-02-21"
print(daysBetweenDates(date7, date8))   #Output: 41646

date9 = "2084-05-19"
date10 = "1976-02-26"
print(daysBetweenDates(date9, date10))   #Output: 39530

date11 = "2003-06-02"
date12 = "2006-12-04"
print(daysBetweenDates(date11, date12))   #Output: 1281