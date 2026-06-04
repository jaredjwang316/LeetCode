"""
Problem Description:
    - You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase 
    English letters and digits).
    - You have to find a permutation of the string where no letter is followed by another letter 
    and no digit is followed by another digit. That is, no two adjacent characters have the same type.
    - Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""

def reformat(s):
    """
    :type s: str
    :rtype: str
    """
    count_digits = 0
    count_letters = 0
    digits = []
    letters = []
    for ch in s:
        if ord(ch) >= 48 and ord(ch) <= 57:
            count_digits += 1
            digits.append(ch)
        elif ord(ch) >= 97 and ord(ch) <= 122:
            count_letters += 1
            letters.append(ch)
    
    if abs(count_digits - count_letters) > 1:
        return ""

    reformatted_string = ""
    if len(digits) < len(letters):
        for i in range(len(digits)):
            reformatted_string = reformatted_string + letters[i] + digits[i]
        reformatted_string += letters[-1]
    elif len(letters) < len(digits):
        for i in range(len(letters)):
            reformatted_string = reformatted_string + digits[i] + letters[i]
        reformatted_string += digits[-1]
    else:
        for i in range(len(letters)):
            reformatted_string = reformatted_string + digits[i] + letters[i]
    
    return reformatted_string

s = "a0b1c2"
print(reformat(s))  #Output: "0a1b2c"

s2 = "leetcode"
if reformat(s2) == "":
    print("Output is an empty string")  #Output: ""

s3 = "1229857369"
if reformat(s3) == "":
    print("Output is an empty string")  #Output: ""