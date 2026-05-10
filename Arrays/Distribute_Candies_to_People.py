"""
Problem Description:
    - We distribute some number of candies, to a row of n = num_people people in the following way:
    - We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies 
    to the last person.  Then, we go back to the start of the row, giving n + 1 candies to the first person, 
    n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.  This process repeats 
    (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run 
    out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the 
    previous gift).
    - Return an array (of length num_people and sum candies) that represents the final distribution of candies.

Constraints:
    - 1 <= candies <= 10^9
    - 1 <= num_people <= 1000
"""

def distributeCandies(candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    distributed_candies = []
    for i in range(num_people):
        distributed_candies.append(0)   #everyone start out with 0 candies
    
    person = 0
    give = 1    #how much candy we give to that person in this iteration
    while(candies > 0):
        amount = min(give, candies) #last person will receive all the remaining candies
        distributed_candies[person] += amount
        candies = candies - amount
        person = (person + 1) % num_people  #move to the start of the row after we reach the end
        give += 1   #give one more candy in the next iteration
    
    return distributed_candies

candies = 7
num_people = 4
print(distributeCandies(candies, num_people))   #Output: [1,2,3,1]

candies2 = 10
num_people2 = 3
print(distributeCandies(candies2, num_people2))   #Output: [5,2,3]