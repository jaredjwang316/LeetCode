"""
Problem Description:
    - There are n rings and each ring is either red, green, or blue. The rings are distributed across 
    ten rods labeled from 0 to 9.
    - You are given a string rings of length 2n that describes the n rings that are placed onto the rods. 
    Every two characters in rings forms a color-position pair that is used to describe each ring where:
        * The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
        * The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
    - For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring 
    placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
    - Return the number of rods that have all three colors of rings on them.

Constraints:
    - rings.length == 2 * n
    - 1 <= n <= 100
    - rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
    - rings[i] where i is odd is a digit from '0' to '9' (0-indexed).
"""

def countPoints(rings):
    """
    :type rings: str
    :rtype: int
    """
    rod_colors = dict()

    for i in range(1, len(rings), 2):
        if rings[i] not in rod_colors:
            rod_colors[ rings[i] ] = set()
            rod_colors[ rings[i] ].add(rings[i - 1])
        else:
            rod_colors[ rings[i] ].add(rings[i - 1])
    
    count = 0
    for k in rod_colors.keys():
        if len(rod_colors[k]) == 3: #if all three colors (R, G, B) of rings are on the rod 
            count += 1
    
    return count

rings = "B0B6G0R6R0R6G9"
print(countPoints(rings))   #Output: 1

rings2 = "B0R0G0R9R0B0G0"
print(countPoints(rings2))   #Output: 1

rings3 = "G4"
print(countPoints(rings3))   #Output: 0
