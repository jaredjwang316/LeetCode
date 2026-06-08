"""
Problem Description:
    - You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive 
    (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
    - Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the 
    ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball 
    number 10 will be put in the box number 1 + 0 = 1.
    - Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

Constraints:
    - 1 <= lowLimit <= highLimit <= 10^5
"""

def digitSum(number):
    sumOfDigits = 0
    while(number > 0):
        sumOfDigits += (number % 10)
        number = number // 10
    return sumOfDigits

def countBalls(lowLimit, highLimit):
    """
    :type lowLimit: int
    :type highLimit: int
    :rtype: int
    """
    boxFreq = dict()
    for i in range(lowLimit, highLimit + 1, 1):
        if digitSum(i) not in boxFreq:
            boxFreq[digitSum(i)] = 1
        else:
            boxFreq[digitSum(i)] += 1
    
    maxVal = -1
    for val in boxFreq.values():
        if val > maxVal:
            maxVal = val
    
    return maxVal

lowLimit = 1
highLimit = 10
print(countBalls(lowLimit, highLimit))    #Expected output: 2

lowLimit2 = 5
highLimit2 = 15
print(countBalls(lowLimit2, highLimit2))    #Expected output: 2

lowLimit3 = 19
highLimit3 = 28
print(countBalls(lowLimit3, highLimit3))    #Expected output: 2