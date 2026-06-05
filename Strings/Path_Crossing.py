"""
Problem Description:
    - Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one 
    unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane 
    and walk on the path specified by path.

    - Return true if the path crosses itself at any point, that is, if at any time you are on a location 
    you have previously visited. Return false otherwise.

Constraints:
    - 1 <= path.length <= 104
    - path[i] is either 'N', 'S', 'E', or 'W'
"""

def isPathCrossing(path):
    """
    :type path: str
    :rtype: bool
    """
    # positive value means north or east while negative value means south or west
    directions = []    #first element of a sublist is vertical direction and second one is horizontal direction

    horizontal_distance = 0 #horizontal distance from origin
    vertical_distance = 0   #vertical distance from origin
    directions.append([vertical_distance, horizontal_distance]) #start at the origin

    for ch in path:
        if ch == 'N':
            vertical_distance += 1
        elif ch == 'S':
            vertical_distance -= 1
        elif ch == 'W':
            horizontal_distance -= 1
        else:   #ch == E case
            horizontal_distance += 1
        
        direction_pair = [vertical_distance, horizontal_distance]
        if direction_pair not in directions:
            directions.append( direction_pair )
        else:
            return True #we touched a point that we previously went to
    
    return False

path = "NESWW"
print(isPathCrossing(path))    #True

path2 = "NES"
print(isPathCrossing(path2))   #False