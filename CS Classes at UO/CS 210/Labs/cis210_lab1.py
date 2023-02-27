'''
CIS 210 Lab 1 - Lab 1 Exercises

Author: Isabella Cortez

Credits: Lab Group

Lab exercises demonstrating how IDLE editor and Shell interact
'''

# greeting = 'hello, Python' 
welcome = 'hello, Python'

def is_even(n):
    '''
    int -> Boolean
    
    Returns True if n is an even number.

    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(0)
    True
    '''

    return (n % 2) == 0

