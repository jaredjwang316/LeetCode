"""
Created on Fri Apr 10 2026

@author: jwang

Problem Description:
    We are given an array asteroids of integers representing asteroids in a row. 
    The indices of the asteroid in the array represent their relative position in space.

    For each asteroid, the absolute value represents its size, and the sign 
    represents its direction (positive meaning right, negative meaning left). Each 
    asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids meet, 
    the smaller one will explode. If both are the same size, both will explode. 
    asteroids moving in the same direction will never meet.

Constraints:
    2 <= asteroids.length <= 10^4
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""

def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    theStack = [asteroids[0]]

    for i in range(1, len(asteroids)):
        if len(theStack) == 0:
            theStack.append(asteroids[i])
            continue
            
        if (theStack[-1] > 0 and asteroids[i] > 0) or (theStack[-1] < 0 and asteroids[i] < 0):
            theStack.append(asteroids[i])
        elif theStack[-1] < 0 and asteroids[i] > 0: #asteroids are opposite in directions but diverging 
            theStack.append(asteroids[i])
        elif theStack[-1] + asteroids[i] == 0:  #equal in size but opposite in direction, both asteroids cancel/negate each other.  They cannot diverge as checked in the previous condition
            theStack.pop()
        elif theStack[-1] > 0 and asteroids[i] < 0: #converging in opposing directions
            flag = True
            while len(theStack) > 0 and theStack[-1] > 0:
                if abs(asteroids[i]) < abs(theStack[-1]):
                    flag = False
                    break   #that current asteroids explodes as its size is smaller
                elif abs(asteroids[i]) == abs(theStack[-1]):    #both asteroids that collided will explode
                    theStack.pop()
                    flag = False
                    break
                else:
                    theStack.pop()
            
            if flag == True:    #the current asteroids did not explode
                theStack.append(asteroids[i])
    return theStack

asteroids = [5,10,-5]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids))  #[5,10] The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

asteroids2 = [8,-8]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids2))  #[] The 8 and -8 collide exploding each other.

asteroids3 = [10,2,-5]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids3))  #[10] The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

asteroids4 = [3, 5, -6, 2, -1, 4]
#The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids4))  #[-6,2,4] 

asteroids5 = [-2,-1,1,2]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids5))  #[-2,-1,1,2]

asteroids6 = [-2,-2,-1,2]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids6))  #[-2,-2,-1,2]

asteroids7 = [1,-1,-2,-2]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids7))  #[-2,-2]

asteroids8 = [-2,-2,1,-1]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids8))  #[-2,-2]

asteroids9 = [13, 17, -5, -10, 8, -8, 15, -20]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids9))  #[-20]

asteroids10 = [-10, -5, -4, 2, 5, 6]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids10))  #[-10, -5, -4, 2, 5, 6]

asteroids11 = [1, 2, 3, 4, 5]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids11))  #[1, 2, 3, 4, 5]

asteroids12 = [1, 3, 5, -6, -9]
print("The state of the asteroids after all collisions is:", asteroidCollision(asteroids12))  #[-6, -9] 