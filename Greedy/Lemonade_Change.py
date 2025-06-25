# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 10:08:48 2025

@author: jwang

Problem Description:
    At a lemonade stand, each lemonade costs $5. Customers are standing in a 
    queue to buy from you and order one at a time (in the order specified by 
    bills). Each customer will only buy one lemonade and pay with either a $5, 
    $10, or $20 bill. You must provide the correct change to each customer so 
    that the net transaction is that the customer pays $5.
    
    Note that you do not have any change in hand at first.
    
    Given an integer array bills where bills[i] is the bill the ith customer pays, 
    return true if you can provide every customer with the correct change, or false otherwise.

Important Constraints:
    1 <= bills.length <= 10^5
    bills[i] is either 5, 10, or 20.

"""

def lemonadeChange( bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    if bills[0] > 5:    #we start out with no change
        return False

    five_dollars = 0
    ten_dollars = 0

    for b in bills:
        if b == 5:  #we do not need to give change
            five_dollars += 1
        elif b == 10:       #we only give $5 of change
            ten_dollars += 1
            if five_dollars <= 0:
                return False
            five_dollars -= 1
        elif b == 20:   #we need to give $15 of change
            if ten_dollars <= 0:    #we could give 3 $5 as change
                if five_dollars < 3:
                    return False
                else:
                    five_dollars -= 3
            else:
                if five_dollars <= 0:
                    return False
                else:
                    ten_dollars -= 1
                    five_dollars -= 1

    return True

bills = [5,5,5,10,20]
print(lemonadeChange(bills))    #True

bills2 = [5,5,10,10,20]
print(lemonadeChange(bills2))   #False