"""
Problem Description:
    You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. 
    Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
    
    The chemistry of a team is equal to the product of the skills of the players on that team.

    Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into 
    teams such that the total skill of each team is equal.
"""

def dividePlayers(skill):
    """
    :type skill: List[int]
    :rtype: int
    """
    skill.sort()
    expected = skill[0] + skill[-1]
    result = skill[0] * skill[-1]
    
    left = 1
    right = len(skill) - 2

    while(left < right):
        if skill[left] + skill[right] != expected:
            return -1
        result = result + skill[left] * skill[right]
        left += 1
        right -= 1

    return result

skill = [3,2,5,1,3,4]
print(dividePlayers(skill))  #22

skill2 = [3,4]
print(dividePlayers(skill2))  #12

skill3 = [1,1,2,3]
print(dividePlayers(skill3))  #-1