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
    visited_points = set()
    visited_points.add( (0, 0) )

    horizontal_direction = 0
    vertical_direction = 0
    
    for ch in path:
        if ch == "N":
            vertical_direction += 1
        elif ch == "S":
            vertical_direction -= 1
        elif ch == "W":
            horizontal_direction -= 1
        else:
            horizontal_direction += 1
        
        if (horizontal_direction, vertical_direction) in visited_points:
            return True
        visited_points.add( (horizontal_direction, vertical_direction) )

    return False

path = "NESWW"
print(isPathCrossing(path))    #True

path2 = "NES"
print(isPathCrossing(path2))   #False