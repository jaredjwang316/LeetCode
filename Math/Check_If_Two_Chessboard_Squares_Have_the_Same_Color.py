"""
Problem Description:
    - You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square 
    on an 8 x 8 chessboard.
    - Return true if these two squares have the same color and false otherwise.
    - The coordinate will always represent a valid chessboard square. The coordinate will always have the 
    letter first (indicating its column), and the number second (indicating its row).

Constraints:
    - coordinate1.length == coordinate2.length == 2
    - 'a' <= coordinate1[0], coordinate2[0] <= 'h'
    - '1' <= coordinate1[1], coordinate2[1] <= '8'
"""

def checkTwoChessboards(coordinate1, coordinate2):
    """
    :type coordinate1: str
    :type coordinate2: str
    :rtype: bool
    """
    # letter 'a' has ascii value of 97, and digit '0' has ascii value of 48

    # coordinate1 is black and coordinate2 is white.  Ex: a1 vs b1
    if ( ord(coordinate1[0]) % 2 == 1 and (ord(coordinate1[1]) - 48) % 2 == 1) and ( ord(coordinate2[0]) % 2 == 0 and (ord(coordinate2[1]) - 48) % 2 == 1):
        return False
    
    # coordinate1 is black and coordinate2 is white.  Ex: a1 vs a2
    if ( ord(coordinate1[0]) % 2 == 1 and (ord(coordinate1[1]) - 48) % 2 == 1) and ( ord(coordinate2[0]) % 2 == 1 and (ord(coordinate2[1]) - 48) % 2 == 0):
        return False   

    # coordinate1 is black and coordinate2 is white.  Ex: b2 vs a2
    if ( ord(coordinate1[0]) % 2 == 0 and (ord(coordinate1[1]) - 48) % 2 == 0) and ( ord(coordinate2[0]) % 2 == 1 and (ord(coordinate2[1]) - 48) % 2 == 0):
        return False

    # coordinate1 is black and coordinate2 is white.  Ex: b2 vs b1
    if ( ord(coordinate1[0]) % 2 == 0 and (ord(coordinate1[1]) - 48) % 2 == 0) and ( ord(coordinate2[0]) % 2 == 0 and (ord(coordinate2[1]) - 48) % 2 == 1):
        return False

    # coordinate1 is white and coordinate2 is black.  Ex: b1 vs b2
    if ( ord(coordinate1[0]) % 2 == 0 and (ord(coordinate1[1]) - 48) % 2 == 1) and ( ord(coordinate2[0]) % 2 == 0 and (ord(coordinate2[1]) - 48) % 2 == 0):
        return False

    # coordinate1 is white and coordinate2 is black.  Ex: b1 vs a1
    if ( ord(coordinate1[0]) % 2 == 0 and (ord(coordinate1[1]) - 48) % 2 == 1) and ( ord(coordinate2[0]) % 2 == 1 and (ord(coordinate2[1]) - 48) % 2 == 1):
        return False    
    
    # coordinate1 is white and coordinate2 is black.  Ex: a2 vs a1
    if ( ord(coordinate1[0]) % 2 == 1 and (ord(coordinate1[1]) - 48) % 2 == 0) and ( ord(coordinate2[0]) % 2 == 1 and (ord(coordinate2[1]) - 48) % 2 == 1):
        return False         

    # coordinate1 is white and coordinate2 is black.  Ex: a2 vs b2
    if ( ord(coordinate1[0]) % 2 == 1 and (ord(coordinate1[1]) - 48) % 2 == 0) and ( ord(coordinate2[0]) % 2 == 0 and (ord(coordinate2[1]) - 48) % 2 == 0):
        return False

    return True

coordinate1 = "a1"
coordinate2 = "c3"
print(checkTwoChessboards(coordinate1, coordinate2))  # Output: True

coordinate3 = "a1"
coordinate4 = "h3"
print(checkTwoChessboards(coordinate3, coordinate4))  # Output: False

coordinate5 = "h7"
coordinate6 = "c8"
print(checkTwoChessboards(coordinate5, coordinate6))  # Output: True

coordinate7 = "h8"
coordinate8 = "c4"
print(checkTwoChessboards(coordinate7, coordinate8))  # Output: False

coordinate9 = "f8"
coordinate10 = "d5"
print(checkTwoChessboards(coordinate9, coordinate10))  # Output: False