"""
Problem Description:
    - You are given a string s consisting of digits. Perform the following operation repeatedly until the 
    string has exactly two digits:
        * For each pair of consecutive digits in s, starting from the first digit, calculate a new digit 
        as the sum of the two digits modulo 10.
        * Replace s with the sequence of newly calculated digits, maintaining the order in which they are 
        computed.
    - Return true if the final two digits in s are the same; otherwise, return false.

Constraints:
    - 3 <= s.length <= 100
    - s consists of only digits.
"""

def hasSameDigits(s):
    """
    :type s: str
    :rtype: bool
    """
    
    new_s = ""
    while(len(s) > 2):
        new_s = ""
        for i in range(len(s) - 1):
            new_s = new_s + str( ( ( ord(s[i]) - 48 ) + ( ord(s[i + 1]) - 48 ) ) % 10)  # 48 represents '0'
        
        s = new_s
    
    if s[0] == s[1]:
        return True
    
    return False

s = "3902"
print(hasSameDigits(s)) #True

s2 = "34789"
print(hasSameDigits(s2))    #False