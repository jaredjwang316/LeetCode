"""
Problem Description:
    - You are given an array bulbs of integers between 1 and 100.
    - There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.
    - For each element bulbs[i] in the array bulbs:
        * If the bulbs[i]th light bulb is currently off, switch it on.
        * Otherwise, switch it off.
    - Return the list of integers denoting the light bulbs that are on in the end, sorted in ascending 
    order. If no bulb is on, return an empty list.

Constraints:
    - 1 <= bulbs.length <= 100
    - 1 <= bulbs[i] <= 100
"""

def toggleLightBulbs(bulbs):
    """
    :type bulbs: List[int]
    :rtype: List[int]
    """
    bulb_status = dict()

    for bulb in bulbs:
        if bulb not in bulb_status: # All bulbs are initially off
            bulb_status[bulb] = True    #Switch the bulb on
        else:
            if bulb_status[bulb] == True:   #if the bulb is currently on
                bulb_status[bulb] = False   #switch it off
            else:   # if the bulb is currently off
                bulb_status[bulb] = True    #switch it on

    result = []
    for k,v in bulb_status.items():
        if v == True:   #if the light bulb is on at the end
            result.append(k)
    
    result.sort()
    return result

bulbs = [10,30,20,10]
print(toggleLightBulbs(bulbs))  #[20, 30]

bulbs2 = [100,100]
if len(toggleLightBulbs(bulbs2)) == 0:
    print("Empty list")
