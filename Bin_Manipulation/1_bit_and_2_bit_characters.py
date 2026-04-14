"""
Problem Description:
    We have two special characters:
        - The first character can be represented by one bit 0.
        - The second character can be represented by two bits (10 or 11).

    Given a binary array bits that ends with 0, return true if the last character 
    must be a one-bit character.

Constraints:
    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.
"""

def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    i = 0
    while(i < len(bits)):
        if i == len(bits) - 1:
            return True
        if bits[i] == 1:    #interpret it as two-bit character
            i += 2
        else:
            i += 1
    return False

case1 = [1, 0, 0]
print(isOneBitCharacter(case1)) # Output: true

case2 = [1, 1, 1, 0]
print(isOneBitCharacter(case2)) # Output: false