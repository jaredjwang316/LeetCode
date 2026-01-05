"""
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
    theStack = []

    for a in range(len(asteroids)):
        while len(theStack) > 0:
            if theStack[-1] < 0 and asteroids[a] < 0:
                break
            if theStack[-1] > 0 and asteroids[a] > 0:
                break

            collision = theStack[-1] + asteroids[a]
            if collision == 0:
                if theStack[-1] > 0 and asteroids[a] < 0:
                    asteroids[a] = 0
                    theStack.pop()
                break
            elif collision > 0:
                if theStack[-1] < 0 and asteroids[a] > 0:   #divergence
                    break
                if asteroids[a] < 0:
                    asteroids[a] = 0
                elif theStack[-1] < 0:
                    theStack.pop()
                break
            else:
                if theStack[-1] < 0 and asteroids[a] > 0:   #divergence
                    break
                if theStack[-1] > 0:
                    theStack.pop()
                else:
                    asteroids[a] = 0
                    break
        if asteroids[a] != 0:
            theStack.append(asteroids[a])
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
