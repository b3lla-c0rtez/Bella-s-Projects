'''
Calculate the Square Root: Sqrt.CIS 210 Project 2-2 Square Root Assignment
Author: Isabella Cortez
Credits: Austin Vierra, Lauren Mathews
Calculate the square root when given the equation and two numbers. Compare it given the number and iterations. Give the percent error as well.
'''

from math import *

def mysqrt (n, k): # function header
    
    '''
    (int, int) -> float

    n = the number for the square root
    k = number of times solution will run
    
    Uses babylonian method to calculate the approximate square root

    >>> mysqrt (7,7)
    2.6457513110645907

    >>> mysqrt (65,5)
    8.067781884133503

    >>> mysqrt (6,3)
    2.454256360078278
    '''
    
    x0 = 1 
    for index in range (k):
        equation = .5 * (x0 + n/x0)
        x0 = equation 

    return equation

def sqrt_compare (num, iterations): # function header
    
    '''
    (int, int) -> int

    num = the number we want to find the square root of
    iterations = number of times the integer

    Takes the caluclator square root
    and the mysqrt functions answer and
    reports their findings then
    finds the percent error

    >>>sqrt_compare (7,8)
    For 7 using 8 iterations:
    mysqrt value is: 2.6457513110645907
    math lib sqrt value is: 2.6457513110645907
    This is a 0.0 percent error

    >>>sqrt_compare (23,11)
    For 23 using 11 iterations:
    mysqrt value is: 4.795831523312719
    math lib sqrt value is: 4.795831523312719
    This is a 0.0 percent error

    >>>sqrt_compare (65,5)
    For 65 using 5 iterations:
    mysqrt value is: 8.067781884133503
    math lib sqrt value is: 8.06225774829855
    This is a 0.07 percent error
    '''
    
    calculator = (sqrt (num))
    my_func = mysqrt (num, iterations)
    error = round(abs(((calculator - my_func) / calculator)) * 100, 2)
    print ("For", num, "using", iterations, "iterations:")
    print ("mysqrt value is:", my_func)
    print ("math lib sqrt value is:", calculator)
    print ("This is a", error, "percent error")
    print('')
    return None

def main(): # function header
    
    '''
    () -> None
    
    Square root comparison program driver.
    '''
    
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()
