''' 
CIS 122 Fall 2020 Assignment 2 Question 2
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews
Description: Create two functions to display the volume of a slab of cement in yards and the thickness, width, and length in inches
'''

import math

# Return cement amount in yard using cubic inch given thickness (t), width (w), and length (l) in inches
def calc_yards_cement ( t, w, l):

    # Defined Variables
    t = t/12
    volume = ( t * w * l)
    yard = (volume / math.pow(3,3))
    
    # Return cement values
    return yard

# Output (print) results calculating yards given thickness (t), width (w), and length (l) in inches
def print_results ( t, w, l):

    # Result string
    resultString = 'A cement slab ' + str(t) + '" thick ' + str(w*12) + '" wide and ' + str(l*12) + '" long requires ' + str(round(calc_yards_cement(t, w, l), 2)) + ' cubic yards of cement'
    
    # Print results
    print (resultString)

# Input values 
print_results(4,4,12)
print_results(4,15,20)
