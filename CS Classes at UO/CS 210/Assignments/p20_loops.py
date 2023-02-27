'''
Work With Loops: Loops.CIS 210 Project 2-0 Looping Assignment
Author: Isabella Cortez
Credits: Austin Vierra, Lauren Mathews
Work with loops to recreate the q6 function using a for loop and the add digits function using a for loop
'''

import math

##def q6():
##    i = 0
##    p = 1
##    while i < 4:
##        i = 1
##        p = p * 2
##        i += 1
##    return p

def q6_better(): # function header
    
    '''
    Rewrites the function q6 to
    make the function work. It
    uses a for loop and it works
    better
                        #Examples of Use

    >>>q6_better()
    16
    '''
    
    i = 0
    p = 1
    for i in range(4):
        i = 1
        p = p * 2
        i += 1
    
    return p

def q6_final(n, m): # function header
    
    '''
    (int, int) -> float
    
    Rewrites the function q6 to
    take in two parameters where
    n is raised to the power of m.
    It uses a for loop.
    
                        #Examples of Use

    >>>q6_final(4,2)
    16.0
    >>>q6_final(3,3)
    27.0
    >>>q6_final(2,2)
    4.0
    '''
    
    for i in range(m):
        power = math.pow(n,m)
    return power


def add_digits2a_better(n): # function header
    
    '''
    (int) -> int
    
    Return the sum of a 3-digit integer.
    The function takes a parameter that has
    3 digits and adds each individual digit.
    It uses a for loop.
                           #EXAMPLES OF USE
    >>> add_digits(789)
    24
    >>> add_digits(101)
    2
    '''
    
    for i in range(n):
         digit1 = n //100 # 7
         get100 = digit1 * 100 #700
         get10 = n - get100 # 89
         digit2 = get10 // 10 # 8
         get1 = digit2 * 10 # 80
         digit3 = n - (get100 + get1)
         answer = digit1 + digit2 + digit3
        
    return answer

def add_digits2b_better(nums): # function header
    
    '''
    (int) -> int
                        
    Return the sum of an integer with any
    number of digits. The function takes a
    parameter that is an integer and adds
    each individual digit of it. It uses
    a for loop. 
                           #EXAMPLES OF USE
    >>> add_digits2(789)
    24
    >>> add_digits2(101)
    2
    >>> add_digits2(000)
    0
    >>> add_digits2(5)
    5
    >>> add_digits2(10101)
    3
    '''
    
    num_sum = 0
    counter = 1
    for counter in range(nums):
        number = nums % 10
        nums = nums // 10
        num_sum += number
        counter += 1
        
    return num_sum
