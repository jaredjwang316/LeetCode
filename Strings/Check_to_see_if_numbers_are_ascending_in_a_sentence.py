"""
Problem Description:
    - A sentence is a list of tokens separated by a single space with no leading or trailing spaces. 
    Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word 
    consisting of lowercase English letters.
        * For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are 
        numbers and the other tokens such as "puppy" are words.
    - Given a string s representing a sentence, you need to check if all the numbers in s are strictly 
    increasing from left to right (i.e., other than the last number, each number is strictly smaller 
    than the number on its right in s).  Return true if so, or false otherwise.
"""

def areNumbersAscending(s):
    """
    :type s: str
    :rtype: bool
    """
    prev_num = -1

    number = ""
    for ch in s:
        if ord(ch) >= 48 and ord(ch) <= 57: #if the character is a digit
            number += ch
        else:
            if number != "":
                if int(number) <= prev_num:
                    return False
                else:
                    prev_num = int(number)
                    number = ""
    
    if number != "":
        if int(number) <= prev_num:
            return False
    
    return True

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
print(areNumbersAscending(s)) # Output: True

s2 = "hello world 5 x 5"
print(areNumbersAscending(s2)) # Output: False

s3 = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(areNumbersAscending(s3)) # Output: False