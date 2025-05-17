# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:10:43 2025

@author: jwang
"""

def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    one_digit_words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 
                        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    two_digit_words = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                        16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 
                        30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    two_dig = [90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    
    hundreds = {100: "One Hundred", 200: "Two Hundred", 300: "Three Hundred", 400: "Four Hundred", 500: "Five Hundred",
                600: "Six Hundred", 700: "Seven Hundred", 800: "Eight Hundred", 900: "Nine Hundred"}
    three_dig = [900, 800, 700, 600, 500, 400, 300, 200, 100]

    if num == 0:
        return "Zero"
    elif num < 10:
        return one_digit_words[num]
    elif num <= 20:
        return two_digit_words[num]
    elif num < 100:
        ty = ""
        if num in two_digit_words.keys():
            return two_digit_words[num]
        else:
            return two_digit_words[((num // 10) * 10)] + " " + one_digit_words[num % 10]
    elif num < 1000:
        hund = ""
        while(num > 0):
            if num >= 100:
                for n in three_dig:
                    if n <= num:
                        hund += hundreds[n]
                        num -= n  
                        break
            elif num >= 10:    
                for n in two_dig:
                    if n <= num:
                        hund += " " + two_digit_words[n]
                        num = num - n 
                        break
            else:
                hund += " " + one_digit_words[num]
                num = 0
        return hund
    elif num < 100000:
        if num < 10000:
            th = one_digit_words[num // 1000] + " Thousand"
            num = num - ( (num // 1000) * 1000)
        else:
            if (num // 1000) in two_digit_words.keys():
                th = two_digit_words[num // 1000] + " Thousand"
            else:
                th = two_digit_words[((num // 10000) * 10)] + " " + one_digit_words[ (num // 1000) % 10] + " Thousand"                
        num = num - ( (num // 1000) * 1000)
        if num > 0:
            th += " " + numberToWords(num)
        return th
    elif num < 1000000: 
        hunth = ""
        while ((num // 1000) > 0 ):
            
            if (num // 1000) >= 100:
                for n in three_dig:
                    if n <= (num // 1000):
                        hunth += hundreds[n]
                        num -= (n * 1000) 
                        break
            elif (num // 1000) >= 10:    
                for n in two_dig:
                    if n <= (num // 1000):
                        hunth += " " + two_digit_words[n]
                        num -= (n * 1000)
                        break
            else:
                hunth += " " + one_digit_words[(num // 1000)] 
                num -= ((num // 1000) * 1000)
                break               
        hunth += " Thousand"
        if num > 0:
            hunth += " " + numberToWords(num)
        return hunth
    elif num < 100000000:   #if less than a hundred million
        ml = ""
        if num < 10000000:
            ml = one_digit_words[num // 1000000] + " Million"
            num = num - ( (num // 1000000) * 1000000)
        else:
            if (num // 1000000) in two_digit_words.keys():
                ml = two_digit_words[num // 1000000] + " Million"
            else:
                ml = two_digit_words[((num // 10000000) * 10)] + " " + one_digit_words[ (num // 1000000) % 10] + " Million"   
        num = num - ( (num // 1000000) * 1000000)
        if num > 0:
            ml += " " + numberToWords(num)
   
        return ml
    elif num < 1000000000:  #if less than a billion
        hmill = ""
        while ((num // 1000000) > 0 ):    
            if (num // 1000000) >= 100:
                for n in three_dig:
                    if n <= (num // 1000000):
                        hmill += hundreds[n]
                        num -= (n * 1000000) 
                        break
            elif (num // 1000000) >= 10:    
                for n in two_dig:
                    if n <= (num // 1000000):
                        hmill += " " + two_digit_words[n]
                        num -= (n * 1000000)
                        break
            else:
                hmill += " " + one_digit_words[(num // 1000000)] 
                num -= ((num // 1000000) * 1000000)
                break               
        hmill += " Million"
        if num > 0:
            hmill += " " + numberToWords(num)    
        return hmill    
    #if number is 1 billion or greater but less than or equal to the max constraints of the problem
    largest = ""
    if num < 2000000000:
        largest = "One Billion"
        num -= 1000000000
    else:
        largest = "Two Billion"
        num = num - 2000000000
    if num > 0:
        largest += " " + numberToWords(num)
    return largest

print(numberToWords(123))
print(numberToWords(12345))
print(numberToWords(1234567))
print(numberToWords(2135468749))


