"""
Problem Description:
    Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards 
    have gone and will come back in H hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and 
    eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will 
    not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:
    1 <= piles.length <= 10^4
    piles.length <= h <= 10^9
    1 <= piles[i] <= 10^9
"""

def canFinish(piles, k, h):
    count = 0
    for pile in piles:
        if pile % k == 0:
            count = count + (pile // k)
        else:
            count = count + (pile // k) + 1
    
    if count <= h:
        return True
    return False

def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    left = 1
    right = max(piles)

    while(left <= right):
        mid = (left + right) // 2
        if canFinish(piles, mid, h) == True:
            right = mid - 1 #check to see if we can find a smaller eating speed that satisfies the condition of finishing the bananas within h hours
        else:
            left = mid + 1  #eating speed can only be faster for there to be a possibility of finishing the bananas within h hours

    return left

# Test Cases
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h)) # Expected Output: 4

piles2 = [30,11,23,4,20]
h2 = 5
print(minEatingSpeed(piles2, h2)) # Expected Output: 30

piles3 = [30,11,23,4,20]
h3 = 6
print(minEatingSpeed(piles3, h3)) # Expected Output: 23