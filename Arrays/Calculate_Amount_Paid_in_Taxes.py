"""
Problem Description:
    - You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax 
    bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound 
    (i.e. upperi-1 < upperi for 0 < i < brackets.length).
    - Tax is calculated as follows:
        * The first upper0 dollars earned are taxed at a rate of percent0.
        * The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
        * The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
        * And so on.
    - You are given an integer income representing the amount of money you earned. Return the amount of money that you 
    have to pay in taxes. Answers within 10^(-5) of the actual answer will be accepted.

Constraints:
    - 1 <= brackets.length <= 100
    - 1 <= upperi <= 1000
    - 0 <= percenti <= 100
    - 0 <= income <= 1000
    - upperi is sorted in ascending order.
    - All the values of upperi are unique.
    - The upper bound of the last tax bracket is greater than or equal to income.
"""

def calculateTax(brackets, income):
    """
    :type brackets: List[List[int]]
    :type income: int
    :rtype: float
    """
    taxes = 0.0
    if income >= brackets[0][0]:
        taxes = taxes + brackets[0][0] * float(brackets[0][1]) / 100
        income = income - brackets[0][0]
    else:
        taxes = taxes + income * float(brackets[0][1]) / 100
        income = 0

    for i in range(1, len(brackets)):
        if income >= (brackets[i][0] - brackets[i - 1][0]):
            taxes = taxes + (brackets[i][0] - brackets[i - 1][0]) * float(brackets[i][1]) / 100
            income = income - (brackets[i][0] - brackets[i - 1][0])
        else:
            taxes = taxes + income * float(brackets[i][1]) / 100
            income = 0
        
        if income == 0:
            break
    
    return taxes

brackets = [[3,50],[7,10],[12,25]]
income = 10
print(calculateTax(brackets, income))  # Output: 2.65

brackets2 = [[1,0],[4,25],[5,50]]
income2 = 2
print(calculateTax(brackets2, income2))  # Output: 0.25

bracket3 = [[2,50]]
income3 = 0
print(calculateTax(bracket3, income3))  # Output: 0.0

