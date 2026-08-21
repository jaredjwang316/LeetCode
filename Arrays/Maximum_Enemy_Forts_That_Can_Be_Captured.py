"""
Problem Description:
    - You are given a 0-indexed integer array forts of length n representing the positions of several forts. 
    forts[i] can be -1, 0, or 1 where:
        * -1 represents there is no fort at the ith position.
        * 0 indicates there is an enemy fort at the ith position.
        * 1 indicates the fort at the ith the position is under your command.
    - Now you have decided to move your army from one of your forts at position i to an empty position j such 
    that:
        * 0 <= i, j <= n - 1
        * The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), 
        forts[k] == 0.
    - While moving the army, all the enemy forts that come in the way are captured.
    Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army, 
    or you do not have any fort under your command, return 0.

Constraints:
    - 1 <= forts.length <= 1000
    - -1 <= forts[i] <= 1
"""

def captureForts(forts):
    """
    :type forts: List[int]
    :rtype: int
    """
    positive_one_pos = -1
    max_capture = 0

    for i in range(len(forts)):
        if forts[i] == 1:
            positive_one_pos = i
        elif forts[i] == -1:
            if positive_one_pos != -1:
                max_capture = max(max_capture, i - positive_one_pos - 1)
            positive_one_pos = -1   #army can only travel through enemy forts
    
    for i in range(len(forts) - 1, -1, -1):
        if forts[i] == 1:
            positive_one_pos = i
        elif forts[i] == -1:
            if positive_one_pos != -1:
                max_capture = max(max_capture, positive_one_pos - i - 1)
            positive_one_pos = -1   #army can only travel through enemy forts

    return max_capture

forts = [1,0,0,-1,0,0,0,0,1]
print(captureForts(forts))  # Output: 4

forts2 = [0,0,1,-1]
print(captureForts(forts2))  # Output: 0

forts3 = [0,-1,-1,0,-1]
print(captureForts(forts3))  # Output: 0

forts4 = [-1,-1,0,1,0,0,1,-1,1,0]
print(captureForts(forts4))  # Output: 1

forts5 = [1,0,0,-1]
print(captureForts(forts5))  # Output: 2

forts6 = [-1,0,-1,0,1,1,1,-1,-1,-1]
print(captureForts(forts6))  # Output: 1

forts7 = [-1,1,1,-1,-1,0,-1,1,0,-1,1,-1,1,0,0,1,1,-1,-1,-1,0,-1,0,1,0,0,-1,-1,0,0,1,1,0,0,1,-1,
          1,-1,1,-1,-1,-1,0,-1,0,1,0,-1,1,0,-1,1,-1,1,0,0,1,0,0,1,0,0,1,0,-1,0,0,0,-1,-1,0,-1,1,
          -1,1,-1,0,1,-1,0,-1,1,0,-1,-1,1,0,0,1,1,0,0,0,1,-1,1,-1,1,0,1,-1,0,1,-1,1,0,0,0,-1,0,1,
          1,0,0,0,0,-1,1,1,1,0,1,1,-1,1,-1,-1,0,-1,0,0,1,0,0,0,0,1,0,0,-1,-1,0,1,1,-1,1,-1,1,1,-1,
          0,1,1,1,-1,-1,-1,-1,0,-1,-1,1,1,0,1,-1,-1,-1,1,0,0,-1,0,0,-1,1,-1,-1,1,1,0,-1,1,0,0,0,-1,
          -1,1,0,1,1,1,-1,0,1,0,0,1,-1,0,1,0,0,0,-1,1,1,1,1,-1,1,-1,1,1,0,0,0,-1,1,-1,1,0,1,1,-1,0,
          -1,0,0,1,1,0,-1,-1,-1,0,0,-1,1,-1,1,1,1,-1,1,1,-1,1,1,1,0,-1,1,-1,0,-1,1,-1,1,0,-1,1,-1,1,
          1,-1,1,-1,1,0,-1,1,-1,-1,-1,-1,-1,0,0,-1,0,1,-1,1,-1,0,0,1,0,1,1,0,0,1,1,-1,0,0,1,0,0,0,-1,
          -1,-1,1,1,-1,-1,-1,1,0,-1,0,1,1,0,1,-1,0,-1,1,0,1,1,-1,0,0,-1,0,-1,1,1,-1,-1,1,-1,0,1,1,1,
          1,0,1,1,1,0,0,-1,0,1,0,0,1,1,-1,1,-1,1,1,0,1,0,1,1,1,1,-1,-1,1,-1,-1,-1,0,0,1,0,1,0,1,0,1,
          -1,0,1,-1,-1,0,1,1,0,0,1,1,1,-1,-1,1,1,0,0,1,-1,-1,0,0,-1,-1,-1,1,0,0,1,0,-1,1,-1,0,1,0,0,
          0,-1,1,0,0,-1,0,-1,1,1,1,0,1,1,1,0,1,1,1,1,-1,0,1,-1,-1,0,-1,-1,0,-1,0,0,0,-1,0,-1,0,1,1,1,
          -1,-1,-1,-1,-1,0,-1,1,1,1,0,-1,1,0,-1,-1,0,1,0,1,-1,0,1,1,1,-1,1,0,-1,-1,-1,0,0,-1,0,-1,-1,
          0,-1,0,0,-1,0,0,0,1,-1,0,0,0,0,-1,-1,1,0,1,1,0,0,1,1,-1,1,-1,1,0,1,0,0,0,-1,1,1,-1,1,0,1,-1,
          0,0,0,-1,0,-1,0,0,0,0,0,0,0,0,-1,-1,1,1,-1,1,1,0,-1,-1,0,-1,1,-1,-1,-1,1,-1,1,0,1,1,-1,1,0,0,
          -1,0,-1,-1,-1,1,0,-1,-1,0,-1,-1,-1,1,-1,1,0,-1,-1,0,1,0,1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,0,1,-1,
          0,1,1,-1,1,1,1,1,1,0,0,-1,0,0,0,1,-1,0,1,0,1,1,-1,-1,0,1,1,-1,-1,1,0,0,-1,-1,-1,0,1,1,1,0,0,1,
          -1,1,1,0,0,0,1,-1,-1,1,0,1,0,1,1,1,-1,0,0,-1,-1,-1,-1,-1,0,1,1,0,0,0,-1,1,0,-1,1,1,1,-1,1,1,1,
          1,1,1,-1,-1,-1,0,1,0,-1,1,-1,0,-1,-1,0,-1,-1,0,-1,-1,1,1,1,0,-1,-1,1,1,0,-1,0,0,1,-1,0,1,-1,0,
          0,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,0,-1,0,-1,-1,-1,-1,0,0,0,-1,-1,0,0,-1,-1,0,-1,0,1,0,-1,
          -1,0,0,-1,1,1,0,-1,1,0,1,0,0,-1,0,-1,0,-1,-1,0,0,0,1,-1,1,0,1,1,0,1,0,1,-1,1,0,-1,-1,1,-1,0,1,
          -1,1,0,1,-1,-1,0,1,1,-1,-1,-1,1,0,-1,1,-1,1,0,-1,-1,0,1,0,-1,-1,0,-1,1,-1,1,1,0,-1,-1,1,-1,-1,
          0,0,-1,-1,1,1,0,0,1,-1,1,0,0,0,0,1,-1,1,1,0,1,-1,-1,1,1,-1,-1,0,1,-1,0,0,1,0,-1,-1,-1,1,-1,0,1,
          -1,-1,-1,0,-1,-1,1,1,1,1,1,-1,1,1,-1,-1,0,-1,1,0,-1,1,0,0,1,1,1,-1,-1,1,1,1,1,0,-1,-1,0,-1,-1,
          -1,1,1,0,-1,0,-1,1,-1,0,-1,0,-1,-1,1,-1,-1,-1,-1,-1,0,-1,1,0,1,1,0,-1,1,0,-1,0,0,1,1,1,1,-1,1,
          1,1,-1,-1,0,0,-1,0,-1,-1,0,0,-1,0,1,0,0,0,1,0,0,0,0,1,-1,1,-1]
print(captureForts(forts7))  # Output: 4