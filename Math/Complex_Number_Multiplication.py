# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:58:02 2025

@author: jwang

Problem Description:
    A complex number can be represented as a string on the form "real+imaginaryi" where:
        - real is the real part and is an integer in the range [-100, 100].
        - imaginary is the imaginary part and is an integer in the range [-100, 100].
        - i^2 == -1.

    Given two complex numbers num1 and num2 as strings, return a string of the 
    complex number that represents their multiplications.

Important Constraints:
    num1 and num2 are valid complex numbers.
"""

def complexNumberMultiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    #split the complex numbers into its real and imaginary parts
    num1_components = num1.split('+')   
    num2_components = num2.split('+')

    real = 0
    imaginary = 0
    for n1 in range(len(num1_components)):
        for n2 in range(len(num2_components)):
            non_imaginary_1 = (num1_components[n1])[0 : len(num1_components[n1]) - 1]   #exclude the i component
            non_imaginary_2 = (num2_components[n2])[0 : len(num2_components[n2]) - 1]   #exclude the i component
            if (n1 == 0 and n2 == 0):
                real += (int(num1_components[n1]) * int(num2_components[n2]))
            elif (n1 == 1 and n2 == 1):
                real += (-1) * (int(non_imaginary_1) * int(non_imaginary_2))    #i^2 = -1
            elif (n1 == 0 and n2 == 1):
                imaginary += (int(num1_components[n1]) * int(non_imaginary_2))
            elif (n1 == 1 and n2 == 0):
                imaginary += ( int(non_imaginary_1) * int(num2_components[n2]) )

    imaginary = str(imaginary)
    result = str(real) + "+" + imaginary + "i"
    return result

num1 = "4+5i"
num2 = "7+-6i"
print(num1, "*", num2, "=", complexNumberMultiply(num1, num2))  #result: 58 + 11i

num3 = "1+1i"
num4 = "1+1i"
print(num3, "*", num4, "=", complexNumberMultiply(num3, num4))  #result: 0+2i

num5 = "1+-1i"
num6 = "1+-1i"
print(num5, "*", num6, "=", complexNumberMultiply(num5, num6))  #result: 0+-2i
