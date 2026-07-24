"""
Problem Description:
    - A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.
    - You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in 
    the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith 
    key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every 
    subsequent key was pressed at the exact time the previous key was released.

    - The tester wants to know the key of the keypress that had the longest duration. The ith keypress 
    had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of 
    releaseTimes[0].

    - Note that the same key could have been pressed multiple times during the test, and these multiple 
    presses of the same key may not have had the same duration.
    - Return the key of the keypress that had the longest duration. If there are multiple such 
    keypresses, return the lexicographically largest key of the keypresses.

Constraints:
    - releaseTimes.length == n
    - keysPressed.length == n
    - 2 <= n <= 1000
    - 1 <= releaseTimes[i] <= 109
    - releaseTimes[i] < releaseTimes[i+1]
    - keysPressed contains only lowercase English letters.
"""

def slowestKey(releaseTimes, keysPressed):
    """
    :type releaseTimes: List[int]
    :type keysPressed: str
    :rtype: str
    """
    maxPress = releaseTimes[0]
    longestPressedKey = keysPressed[0]

    for i in range(1, len(releaseTimes)):
        if releaseTimes[i] - releaseTimes[i - 1] > maxPress:
            maxPress = releaseTimes[i] - releaseTimes[i - 1]
            longestPressedKey = keysPressed[i]
        elif releaseTimes[i] - releaseTimes[i - 1] == maxPress: #if there are multiple such keypresses with the longest duration
            if ord(keysPressed[i]) > ord(longestPressedKey):    # return the lexicographically largest key of the keypresses
                longestPressedKey = keysPressed[i]

    return longestPressedKey

releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
print(slowestKey(releaseTimes, keysPressed))  # Output: "c"

releaseTimes2 = [12,23,36,46,62]
keysPressed2 = "spuda"
print(slowestKey(releaseTimes2, keysPressed2))  # Output: "a"