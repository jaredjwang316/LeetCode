"""
Problem Description:
    - You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each 
    CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, 
    but there's a constraint: there has to be a gap of at least n intervals between two tasks with the 
    same label.

    - Return the minimum number of CPU intervals required to complete all tasks.

Constraints:
    - 1 <= tasks.length <= 10^4
    - tasks[i] is an uppercase English letter.
    - 0 <= n <= 100
"""

def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    task_freq = dict()
    for task in tasks:
        if task not in task_freq:
            task_freq[task] = 1
        else:
            task_freq[task] += 1

    maxFreq = 0
    for val in task_freq.values():
        if val > maxFreq:
            maxFreq = val
    
    count_task_with_max_freq = 0
    for val in task_freq.values():
        if val == maxFreq:
            count_task_with_max_freq += 1

    return max(len(tasks), (maxFreq - 1) * (n + 1) + count_task_with_max_freq)

tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks, n))   #8 -> A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

task2 = ["A","C","A","B","D","B"]
n2 = 1
print(leastInterval(task2, n2))   #6 -> A possible sequence is: A -> B -> C -> D -> A -> B.

tasks3 = ["A","A","A","B","B","B"]
n3 = 3
print(leastInterval(tasks3, n3))   #10 -> A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

        
