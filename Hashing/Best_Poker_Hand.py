"""
Problem Description:
    - You are given an integer array ranks and a character array suits. You have 5 cards where the ith card 
    has a rank of ranks[i] and a suit of suits[i].

    - The following are the types of poker hands you can make from best to worst:

        * "Flush": Five cards of the same suit.
        * "Three of a Kind": Three cards of the same rank.
        * "Pair": Two cards of the same rank.
        * "High Card": Any single card.

    - Return a string representing the best type of poker hand you can make with the given cards.
    - Note that the return values are case-sensitive.

Constraints:
    - ranks.length == suits.length == 5
    - 1 <= ranks[i] <= 13
    - 'a' <= suits[i] <= 'd'
    - No two cards have the same rank and suit.
"""

def bestHand(ranks, suits):
    """
    :type ranks: List[int]
    :type suits: List[str]
    :rtype: str
    """
    suits.sort()
    count_equal_suit = 1
    for s in range(1, len(suits)):
        if suits[s] == suits[s - 1]:
            count_equal_suit += 1
    
    if count_equal_suit == len(suits):
        return "Flush"
    
    rank_freq = dict()
    for rank in ranks:
        if rank not in rank_freq:
            rank_freq[rank] = 1
        else:
            rank_freq[rank] += 1

    freq_list = []
    for val in rank_freq.values():
        freq_list.append(val)
    freq_list.sort()

    for i in range(len(freq_list) - 1, -1, -1):
        if freq_list[i] >= 3:
            return "Three of a Kind"
        elif freq_list[i] == 2:
            return "Pair"
    
    return "High Card"

ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]
print(bestHand(ranks, suits))   # Output: "Flush"

ranks2 = [4,4,2,4,4]
suits2 = ["d","a","a","b","c"]
print(bestHand(ranks2, suits2))  # Output: "Three of a Kind

ranks3 = [10,10,2,12,9]
suits3 = ["a","b","c","a","d"]
print(bestHand(ranks3, suits3))  # Output: "Pair"