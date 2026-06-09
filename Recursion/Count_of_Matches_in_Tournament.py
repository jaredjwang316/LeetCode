"""
Problem Description:
    - You are given an integer n, the number of teams in a tournament that has strange rules:
        * If the current number of teams is even, each team gets paired with another team. A total 
        of n / 2 matches are played, and n / 2 teams advance to the next round.
        * If the current number of teams is odd, one team randomly advances in the tournament, and the
        rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance 
        to the next round.
    - Return the number of matches played in the tournament until a winner is decided.

Constraints:
    - 1 <= n <= 200
"""

def numberOfMatches(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1:  #when one match occurs, that team is considered the winner
        return 0

    if n % 2 == 0:  #if current number of teams is even
        return (n // 2) + self.numberOfMatches(n // 2) #n // 2 matches are played and n // 2 team advances
    return (n // 2) + self.numberOfMatches(n // 2 + 1) #if current number of teams is odd, a total of (n - 1) / 2 matches are played (n - 1) / 2 + 1 teams advance to the next round.

n = 7
print(numberOfMatches(n))    #6

n2 = 14
print(numberOfMatches(n2))    #13