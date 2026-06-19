"""
Problem Description:
    - A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
    - Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Constraints:
    - 1 <= n <= 250
"""

def isPerfectSquare(n):
    i = 0
    while(i * i < n):
        i += 1

    if i * i == n:  #n is a perfect square
        return [i, True]
    
    return [i, False]
def countTriples(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n, 1):
        for j in range(i + 1, n, 1):
            if isPerfectSquare(pow(i, 2) + pow(j, 2))[0] <= n and isPerfectSquare(pow(i, 2) + pow(j, 2))[1] == True:
                count += 2
    
    return count

n = 5
print(countTriples(n))   #2

n2 = 10
print(countTriples(n2))   #4

n3 = 18
print(countTriples(n3))   #10

n4 = 230
print(countTriples(n4))   #302

n5 = 226
print(countTriples(n5))   #298