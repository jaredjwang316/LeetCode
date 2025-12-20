"""
You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each 
lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at 
the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. 
Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this 
process until you have written all of s.

Return an array result of length 2 where:
    result[0] is the total number of lines.
    result[1] is the width of the last line in pixels.
"""

def numberOfLines(widths, s):
    """
    :type widths: List[int]
    :type s: str
    :rtype: List[int]
    """
    line_count = 1
    pixel_length = 0
    for ch in range(len(s)):
        #Note: the ASCII value for 'a' is 97
        if (pixel_length + (widths[ ord(s[ch]) - 97 ]) ) <= 100:
            pixel_length += (widths[ ord(s[ch]) - 97  ])
        else:
            line_count += 1
            pixel_length = (widths[ord(s[ch]) - 97 ])
    
    return [line_count, pixel_length]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
print(numberOfLines(widths, s))   #[3, 60]

widths1 = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s1 = "bbbcccdddaaa"
print(numberOfLines(widths1, s1))   #[2, 4]