'''
Counting Substrings: sscount.CIS 210 Project 3-4 Substring Assignment
Author: Isabella Cortez
Credits: Lauren Mathews, Tori Walters, Austin Vierra
create a function that sees how many times the needle is repeated, one is with an if in function and the other one is a with a boolean/is an if true function
'''

def sscount0(needle, haystack):
    '''
    (string, string) -> int

    needle = substring you are counting
    haystack = the string you are searching for occurences of needle in

    Searches over the string haystack to see how many times the string needle
    is repeated within
    
    >>> sscount1 ("aaa","aaaaa")
    3
    >>> sscount0 ("r","terrorize")
    3
    >>> sscount0 ("mirror","mirror")
    1    
    '''
    
    counter = 0

    for char in range(len(haystack)):
        if needle in (haystack [char :len(needle)+char]):

            counter += 1 
    return counter

def sscount1(needle, haystack):
    '''
    (string, string) -> int

    needle = substring you are counting
    haystack = the string you are searching for occurences of needle in
    
    Searches over the string haystack to see how many times the string needle
    is repeated within
    
    >>> sscount1 ("aaa","aaaaa")
    3
    >>> sscount0 ("r","terrorize")
    3
    >>> sscount0 ("mirror","mirror")
    1    
    
    '''
    
    counter = 0
    for char in range(len(haystack)):
        if haystack.startswith(needle, char) == True:
            counter += 1

    return counter
