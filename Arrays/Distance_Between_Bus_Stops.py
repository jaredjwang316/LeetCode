"""
Problem Description:
    A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs 
    of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

    The bus goes along both directions i.e. clockwise and counterclockwise.
    Return the shortest distance between the given start and destination stops.

Constraints:
    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4
"""

def distanceBetweenBusStops(distance, start, destination):
    """
    :type distance: List[int]
    :type start: int
    :type destination: int
    :rtype: int
    """
    distance_sum = 0
    if start > destination:
        temp = start
        start = destination
        destination = temp
    for num in range(start, destination):
        distance_sum += distance[num]
    
    return min(distance_sum, sum(distance) - distance_sum)  #bus can go clockwise or counterclockwise

distance = [1,2,3,4]
start = 0
destination = 1
print("Shortest distance between the given start and destination stops is:", distanceBetweenBusStops(distance, start, destination)) # 1

distance2 = [1,2,3,4]
start2 = 0
destination2 = 2
print("Shortest distance between the given start and destination stops is:", distanceBetweenBusStops(distance2, start2, destination2)) # 3

distance3 = [1,2,3,4]
start3 = 0
destination3 = 3
print("Shortest distance between the given start and destination stops is:", distanceBetweenBusStops(distance3, start3, destination3)) # 4

distance4 = [7,10,1,12,11,14,5,0]
start4 = 7
destination4 = 2
print("Shortest distance between the given start and destination stops is:", distanceBetweenBusStops(distance4, start4, destination4)) # 17