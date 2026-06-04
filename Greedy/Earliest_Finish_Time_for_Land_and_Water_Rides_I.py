"""
Problem Description:
    - You are given two categories of theme park attractions: land rides and water rides.
    - Land rides
        * landStartTime[i] – the earliest time the ith land ride can be boarded.
        * landDuration[i] – how long the ith land ride lasts.
    - Water rides
        * waterStartTime[j] – the earliest time the jth water ride can be boarded.
        * waterDuration[j] – how long the jth water ride lasts.

- A tourist must experience exactly one ride from each category, in either order.
    * A ride may be started at its opening time or any later moment.
    * If a ride is started at time t, it finishes at time t + duration.
    * Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

- Return the earliest possible time at which the tourist can finish both rides.
"""

def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
    """
    :type landStartTime: List[int]
    :type landDuration: List[int]
    :type waterStartTime: List[int]
    :type waterDuration: List[int]
    :rtype: int
    """
    earliestCompletion = float('inf')
    completionTime = 0
    #start with land ride, then water ride
    for l in range(len(landStartTime)):
        for w in range(len(waterStartTime)):
            completionTime = landStartTime[l] + landDuration[l]
            if completionTime >= waterStartTime[w]: #can you start immediately?
                completionTime += waterDuration[w]
            else:   #other ride has not opened yet thus we need to wait
                completionTime = waterStartTime[w] + waterDuration[w]
            earliestCompletion = min(earliestCompletion, completionTime)
    
    #start with water ride, then land ride
    for w in range(len(waterStartTime)):
        for l in range(len(landStartTime)):
            completionTime = waterStartTime[w] + waterDuration[w]
            if completionTime >= landStartTime[l]:  #can you start immediately?
                completionTime += landDuration[l]
            else:   #other ride is not yet available
                completionTime = landStartTime[l] + landDuration[l]
            earliestCompletion = min(earliestCompletion, completionTime)
    
    return earliestCompletion

landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]
print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))   #Output: 9

landStartTime2 = [5]
landDuration2 = [3]
waterStartTime2 = [1]
waterDuration2 = [10]
print(earliestFinishTime(landStartTime2, landDuration2, waterStartTime2, waterDuration2))   #Output: 14

landStartTime3 = [1]
landDuration3 = [10]
waterStartTime3 = [5]
waterDuration3 = [3]
print(earliestFinishTime(landStartTime3, landDuration3, waterStartTime3, waterDuration3))   #Output: 14