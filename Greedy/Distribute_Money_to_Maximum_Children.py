"""
Problem Description:
    - You are given an integer money denoting the amount of money (in dollars) that you have and another integer 
    children denoting the number of children that you must distribute the money to.
    - You have to distribute the money according to the following rules:
        - All money must be distributed.
        - Everyone must receive at least 1 dollar.
        - Nobody receives 4 dollars.
    - Return the maximum number of children who may receive exactly 8 dollars if you distribute the money 
    according to the aforementioned rules. If there is no way to distribute the money, return -1.

Constraints:
    - 1 <= money <= 200
    - 2 <= children <= 30
"""

def distMoney(money, children):
    """
    :type money: int
    :type children: int
    :rtype: int
    """
    money = money - children
    if money < 0:   #not possible to ensure every children receives some money
        return -1
    
    #at this point, we only need to give 7 dollars to each children for them to receive exactly 8 dollars
    if money % 7 == 0 and money // 7 == children:   #all children can get exactly 8 dollars
        return children

    if money // 7 == children - 1 and money % 7 == 3:   #in this case, last child will get 4 dollars which is against the rule
        return children - 2

    if money // 7 >= children:   #if we make all children get exactly 8 dollars, we are unable to distribute all the money
        return children - 1

    return money // 7

money = 20
children = 3
print(distMoney(money, children)) # 1

money2 = 16
children2 = 2
print(distMoney(money2, children2)) # 2

money3 = 17
children3 = 2
print(distMoney(money3, children3)) # 1

money4 = 18
children4 = 2
print(distMoney(money4, children4)) # 1

money5 = 23
children5 = 2
print(distMoney(money5, children5)) # 1

money6 = 3
children6 = 2
print(distMoney(money6, children6)) # 0

money7 = 2
children7 = 2
print(distMoney(money7, children7)) # 0

money8 = 8
children8 = 2
print(distMoney(money8, children8)) # 0

money9 = 24
children9 = 3
print(distMoney(money9, children9)) # 3

money10 = 18
children10 = 3
print(distMoney(money10, children10)) # 2