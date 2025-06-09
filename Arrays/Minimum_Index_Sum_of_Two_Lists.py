# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 14:49:19 2025

@author: jwang

Problem Description:
    Given two arrays of strings list1 and list2, find the common strings 
    with the least index sum.  A common string is a string that appeared in 
    both list1 and list2.
    A common string with the least index sum is a common string such that if 
    it appeared at list1[i] and list2[j] then i + j should be the minimum value
    among all the other common strings.

    Return all the common strings with the least index sum. Return the answer in any order.

Important Constraints:
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the strings of list1 are unique.
    All the strings of list2 are unique.
    There is at least a common string between list1 and list2.
"""

def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    list1_word_indices = dict()
    list2_word_indices = dict()

    for i in range(len(list1)):
        list1_word_indices[list1[i]] = i
    
    for i in range(len(list2)):
        list2_word_indices[list2[i]] = i

    result = []
    min_sum = pow(2, 31) - 1    #stores the least index sum of common strings        
    for word in list1_word_indices.keys():
        if word in list2_word_indices.keys():
            min_sum = min(min_sum, list1_word_indices[word] + list2_word_indices[word])
    
    for word in list1_word_indices.keys():
        if word in list2_word_indices.keys():
            if list1_word_indices[word] + list2_word_indices[word] == min_sum:
                result.append(word)
    return result

list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print("Common words in the list are:", findRestaurant(list1, list2))

list3 = ["Shogun","Tapioca Express","Burger King","KFC"]
list4 = ["KFC","Shogun","Burger King"]
print("Common words in the list are:", findRestaurant(list3, list4))

list5 = ["happy","sad","good"]
list6 = ["sad","happy","good"]
print("Common words in the list are:", findRestaurant(list5, list6))
