"""
Problem Description:
    - Given a date, return the corresponding day of the week for that date.
    - The input is given as three integers representing the day, month and year respectively.
    - Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", 
    "Thursday", "Friday", "Saturday"}.
    - Note: January 1, 1971 was a Friday.

Constraints:
    - The given dates are valid dates between the years 1971 and 2100.
"""

def isLeapYear(year):
    if year % 100 == 0 and year % 400 != 0: #year is divisible by 100 but not 400
        return False
    if year % 4 != 0:
        return False
    return True

def dayOfTheWeek(day, month, year):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: str
    """
    date_mapping = {
        0 : "Friday", 1 : "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday"
    }
    count_days = 0
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for yr in range(1971, year):
        if isLeapYear(yr) == True:
            count_days += 366
        else:
            count_days += 365
    
    for mn in range(1, month):
        count_days += days_in_month[mn - 1]

    if isLeapYear(year) == True and month >= 3:
        count_days += 1 #account for February 29th date in that current year

    count_days += day
    count_days -= 1 #January 1, 1971 is a Friday
    return date_mapping[count_days % 7]

day = 31
month = 8
year = 2019
print(dayOfTheWeek(day, month, year))   #Output: "Saturday"

day2 = 18
month2 = 7
year2 = 1999
print(dayOfTheWeek(day2, month2, year2))   #Output: "Sunday"

day3 = 15
month3 = 8
year3 = 1993
print(dayOfTheWeek(day3, month3, year3))   #Output: "Sunday"

day4 = 8
month4 = 1
year4 = 1971
print(dayOfTheWeek(day4, month4, year4))   #Output: "Friday"