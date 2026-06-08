"""
Problem Description:
    - You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, 
    where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
        * numberOfBoxesi is the number of boxes of type i.
        * numberOfUnitsPerBoxi is the number of units in each box of the type i.
    - You are also given an integer truckSize, which is the maximum number of boxes that can be put on 
    the truck. You can choose any boxes to put on the truck as long as the number of boxes does not 
    exceed truckSize.
    - Return the maximum total number of units that can be put on the truck.

Constraints:
    - 1 <= boxTypes.length <= 1000
    - 1 <= numberOfBoxes[i] <= 1000
    - 1 <= numberOfUnitsPerBox[i] <= 1000
    - 1 <= truckSize <= 10^6
"""

def maximumUnits(boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    optimal_weight = 0

    boxTypes.sort(key = lambda x: x[1])

    count_boxes = 0
    for i in range(len(boxTypes) - 1, -1, -1):
        if count_boxes + boxTypes[i][0] <= truckSize:   #check if we fit in all the boxes that have boxTypes[i][1] units
            optimal_weight = optimal_weight + boxTypes[i][0] * boxTypes[i][1]
        else:
            optimal_weight = optimal_weight + boxTypes[i][1] * (truckSize - count_boxes)
            break
        count_boxes += boxTypes[i][0]

    return optimal_weight

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(maximumUnits(boxTypes, truckSize))    #Expected output: 8

boxTypes2 = [[5,10],[2,5],[4,7],[3,9]]
truckSize2 = 10
print(maximumUnits(boxTypes2, truckSize2))    #Expected output: 91