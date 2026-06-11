"""
Problem Description:
    - Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
    - He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put 
    in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
    - Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Constraints:
    - 1 <= n <= 1000
"""

def totalMoney(n):
    """
    :type n: int
    :rtype: int
    """
    fullWeeks = n // 7
    remainingDays = n % 7
    
    total_money = 28 * fullWeeks + ((7 * fullWeeks * (fullWeeks - 1)) // 2)  

    for i in range(fullWeeks + 1, fullWeeks + 1 + remainingDays, 1):
        total_money += i
    return total_money

n = 4
print(totalMoney(n))  # Output: 10

n2 = 10
print(totalMoney(n2))  # Output: 37

n3 = 20
print(totalMoney(n3))  # Output: 96

n4 = 26
print(totalMoney(n4))  # Output: 135