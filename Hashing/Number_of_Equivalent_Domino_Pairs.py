"""
Problem Description:
    - Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if 
    either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal 
    to another domino.

    - Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent 
    to dominoes[j].

Constraints:
    - 1 <= dominoes.length <= 4 * 10^4
    - dominoes[i].length == 2
    - 1 <= dominoes[i][j] <= 9
"""

def numEquivDominoPairs(dominoes):
    """
    :type dominoes: List[List[int]]
    :rtype: int
    """
    domino_keys = dict()
    count_pairs = 0

    for domino in dominoes:
        key = 10 * min(domino[0], domino[1]) + max(domino[0], domino[1])
        if key not in domino_keys:
            domino_keys[key] = 1
        else:
            count_pairs += domino_keys[key]
            domino_keys[key] += 1
    
    return count_pairs

dominoes = [[1,2],[2,1],[3,4],[5,6]]
print("number of equivalent domino pairs:", numEquivDominoPairs(dominoes))  # expected output: 1

dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print("number of equivalent domino pairs:", numEquivDominoPairs(dominoes2))  # expected output: 3