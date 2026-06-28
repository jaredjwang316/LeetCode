"""
Problem Description:
    - Given a string s containing only lowercase English letters and the '?' character, convert all 
    the '?' characters into lowercase letters such that the final string does not contain any 
    consecutive repeating characters. You cannot modify the non '?' characters.
    - It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
    - Return the final string after all the conversions (possibly zero) have been made. If there is 
    more than one solution, return any of them. It can be shown that an answer is always possible 
    with the given constraints.

Constraints:
    - 1 <= s.length <= 100
    - s consist of lowercase English letters and '?'.
"""

def modifyString(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
        if s[0] == "?":
            return "a"
        else:
            return s
    
    s_list = list(s)
    for i in range(len(s_list)):
        left_neighbor = ""
        right_neighbor = ""

        if s[i] == "?":
            if i == 0:
                right_neighbor = s_list[i + 1]
            elif i == len(s_list) - 1:
                left_neighbor = s_list[i - 1]
            else:
                right_neighbor = s_list[i + 1]
                left_neighbor = s_list[i - 1]
            
            for j in range(97, 123, 1):
                if chr(j) != left_neighbor and chr(j) != right_neighbor:
                    s_list[i] = chr(j)
                    break
    
    return "".join(s_list)

s = "?zs"
print(modifyString(s))  #output: azs

s2 = "ubv?w"
print(modifyString(s2)) #output: ubvaw
