"""
Problem Description:
    - You are given a string num representing a large integer. An integer is good if it meets the 
    following conditions:
        * It is a substring of num with length 3.
        * It consists of only one unique digit.
    - Return the maximum good integer as a string or an empty string "" if no such integer exists.
    - Note:
        * A substring is a contiguous sequence of characters within a string.
        * There may be leading zeroes in num or a good integer.

Constraints:
    - 3 <= num.length <= 1000
    - num only consists of digits.
"""

def largestGoodInteger(num):
    """
    :type num: str
    :rtype: str
    """
    maxGoodInteger = ""

    count_consecutive = 1
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            count_consecutive += 1
            if count_consecutive == 3:
                if num[i - 2:i + 1] > maxGoodInteger:
                    maxGoodInteger = num[i - 2:i + 1]
        else:
            count_consecutive = 1
    
    if count_consecutive >= 3:
        if num[-3:] > maxGoodInteger:
            maxGoodInteger = num[-3:]
    
    return maxGoodInteger

num = "6777133339"
print(largestGoodInteger(num))  # Output: "777"

num2 = "2300019"
print(largestGoodInteger(num2))  # Output: "000"

num3 = "42352338"
if len(largestGoodInteger(num3)) == 0:
    print("Results in an empty string")
