"""
Problem Description:
    - Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Constraints:
    - date.length == 10
    - date[4] == date[7] == '-', and all other date[i]'s are digits
    - date represents a calendar date between Jan 1st, 1900 and Dec 31st, 2019.
"""

def isLeapYear(year: int) -> bool:
    if year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 != 0:
        return False
    
    return True

def dayOfYear(date: str) -> int:
    date_components = date.split("-")
    days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    count_days = 0
    if isLeapYear(int(date_components[0])) == True:
        days_in_a_month[1] = 29 #leap year case
    
    for m in range(1, int(date_components[1])): #for all the full months that passed by from that date in this year
        count_days += days_in_a_month[m - 1]
    
    count_days += int(date_components[2])   #count the remaining dates that passed by in the current month
    return count_days

date = "2019-01-09"
print(dayOfYear(date)) #Output: 9

date2 = "2019-02-10"
print(dayOfYear(date2)) #Output: 41

date3 = "2004-03-01"
print(dayOfYear(date3)) #Output: 61

date4 = "2012-01-02"
print(dayOfYear(date4)) #Output: 2

date5 = "1900-05-02"
print(dayOfYear(date5)) #Output: 122

