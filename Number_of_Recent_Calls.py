# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 23:51:41 2025

@author: jwang

Problem Description:
    You have a RecentCounter class which counts the number of recent requests 
    within a certain time frame.
    Implement the RecentCounter class:
        - RecentCounter() Initializes the counter with zero recent requests.
        - int ping(int t) Adds a new request at time t, where t represents some 
        time in milliseconds, and returns the number of requests that has 
        happened in the past 3000 milliseconds (including the new request). 
        Specifically, return the number of requests that have happened in the 
        inclusive range [t - 3000, t].
    
    It is guaranteed that every call to ping uses a strictly larger value of t 
    than the previous call.

Constraints:
    1 <= t <= 10^9
    Each test case will call ping with strictly increasing values of t.
    At most 104 calls will be made to ping.
"""

class RecentCounter(object):

    def __init__(self):
        self.recent_requests = 0
        self.theQueue = []
    
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t <= 3000:
            self.recent_requests += 1
            self.theQueue.append(t)
        else:
            if len(self.theQueue) == 0:
                self.theQueue.append(t)
                self.recent_requests += 1
            else:
                while(len(self.theQueue) > 0 and self.theQueue[0] < t - 3000):
                    self.theQueue.remove(self.theQueue[0])
                    self.recent_requests -= 1
                self.recent_requests += 1
                self.theQueue.append(t)

        return self.recent_requests


obj = RecentCounter()

inputs = [1, 100, 3001, 3002]
outputs = []
for t in inputs:
    outputs.append(obj.ping(t))
print("Outputs: ", outputs) #[1, 2, 3, 3]

obj2 = RecentCounter()

inputs2 = [642, 1849, 4921, 5936, 5957]
outputs2 = []
for t in inputs2:
    outputs2.append(obj2.ping(t))
print("Outputs here:", outputs2) #[1, 2, 1, 2, 3]
