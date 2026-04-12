"""
Problem Description:
    Given an array of strings strs, group anagrams together.  You can return the answer in any order.

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100  
    strs[i] consists of lowercase English letters.
"""

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    group_anagrams_dict = dict()
    for string in strs:
        sorted_string = "".join(sorted(string))
        if sorted_string not in group_anagrams_dict:
            group_anagrams_dict[sorted_string] = [string]
        else:
            group_anagrams_dict[sorted_string].append(string)
    
    grouped_result = []
    for val in group_anagrams_dict.values():
        grouped_result.append(val)

    return grouped_result

case1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(case1)) # [["bat"],["nat","tan"],["ate","eat","tea"]]

case2 = [""]
print(groupAnagrams(case2)) # [[""]]

case3 = ["a"]
print(groupAnagrams(case3)) # [["a"]]

