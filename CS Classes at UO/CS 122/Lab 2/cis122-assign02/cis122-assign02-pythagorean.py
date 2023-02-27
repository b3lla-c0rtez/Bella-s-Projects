''' 
CIS 122 Fall 2020 Assignment 2 Question 1
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews
Description: Create two functions to calculate pythagorean theorem given side values for a, b, or c
'''

import math

# Calculate missing side c
def calc_side_c ( a, b ):

    # Return Side C
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# Print Side C
print("c = " , round(calc_side_c (5, 10), 2))

# Calculate missing side a or b
def calc_side_ab ( ab, c ):

    # Return any side
    return math.sqrt(math.pow(c, 2) - math.pow(ab, 2))

# Print any side
print("a/b = " , round(calc_side_ab (4, 8), 2))
