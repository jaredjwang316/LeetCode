"""
Problem Description:
    - There are n employees, each with a unique id from 0 to n - 1.

    - You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
        * idi is the id of the employee that worked on the ith task, and
        * leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei 
        are unique.

    - Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task 
    starts at time 0.

    - Return the id of the employee that worked the task with the longest time. If there is a tie 
    between two or more employees, return the smallest id among them.

Constraints:
    - 2 <= n <= 500
    - 1 <= logs.length <= 500
    - logs[i].length == 2
    - 0 <= idi <= n - 1
    - 1 <= leaveTimei <= 500
    - idi != idi+1
    - leaveTimei are sorted in a strictly increasing order.
"""

def hardestWorker(n, logs):
    """
    :type n: int
    :type logs: List[List[int]]
    :rtype: int
    """
    longestTaskTime = logs[0][1]
    longestEmployee = logs[0][0]

    for i in range(1, len(logs)):
        if logs[i][1] - logs[i - 1][1] > longestTaskTime:
            longestTaskTime = logs[i][1] - logs[i - 1][1]
            longestEmployee = logs[i][0]
        elif logs[i][1] - logs[i - 1][1] == longestTaskTime:
            longestEmployee = min(longestEmployee, logs[i][0])  # If there is a tie between two or more employees, return the smallest id among them.
    
    return longestEmployee

n = 10
logs = [[0,3],[2,5],[0,9],[1,15]]
print(hardestWorker(n, logs))  # Output: 1

n2 = 26
logs2 = [[1,1],[3,7],[2,12],[7,17]]
print(hardestWorker(n2, logs2))  # Output: 3

n3 = 2
logs3 = [[0,10],[1,20]]
print(hardestWorker(n3, logs3))  # Output: 0

n4 = 70
logs4 = [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]
print(hardestWorker(n4, logs4))  # Output: 12