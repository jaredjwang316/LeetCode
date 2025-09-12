# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 22:44:08 2025

@author: jwang

Problem Description:
    The Leetcode file system keeps a log each time some user performs a change 
    folder operation.
    The operations are described below:
    
        "../" : Move to the parent folder of the current folder. (If you are 
                already in the main folder, remain in the same folder).
        "./" : Remain in the same folder.
        "x/" : Move to the child folder named x (This folder is guaranteed to 
                always exist).
    
    You are given a list of strings logs where logs[i] is the operation performed 
    by the user at the ith step.
    
    The file system starts in the main folder, then the operations in logs are performed.
    
    Return the minimum number of operations needed to go back to the main folder 
    after the change folder operations.

Constraints:
    1 <= logs.length <= 103
    2 <= logs[i].length <= 10
    logs[i] contains lowercase English letters, digits, '.', and '/'.
    logs[i] follows the format described in the statement.
    Folder names consist of lowercase English letters and digits.
"""

def minOperations(logs):
    """
    :type logs: List[str]
    :rtype: int
    """
    directory_stack = []

    for log in logs:
        if log == "../":    
            if len(directory_stack) > 0:    
                directory_stack.pop()   #go to the parent folder
            else:   #if already in the main folder
                continue    #stay in that folder
        elif log == "./":   #remain in the same folder
            continue
        else:
            directory_stack.append(log)
    
    return len(directory_stack)

logs = ["d1/","d2/","../","d21/","./"]
print(minOperations(logs))  #2

logs2 = ["d1/","d2/","./","d3/","../","d31/"]
print(minOperations(logs2)) #3

logs3 = ["d1/","../","../","../"]
print(minOperations(logs3)) #0

