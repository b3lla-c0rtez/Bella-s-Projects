'''
Testing Functions: testfuncs.CIS 210 Project 4-1 Testing Substring Assignment
Author: Isabella Cortez
Credits: Lauren Mathews, Tori Walters, Austin Vierra
create functions that test to see if the substring functions from 3-4 are correct
'''

import p34_sscount as p34 

def test_sscount(f, args, expected_result):
    '''(function, string, interger) -> string


    f = function either sscount0 or sscount1
    args = the 2 strings seperated by a space
    expected_result = the estimated answer to sscount

    This function calls sscount0 or sscount1 and then compares its
    results with the user defined expected_result, printing a
    statement determining whether the expected_result is correct or not

    >>> test_sscount (p34.sscount0, 'sses assesses', 2)
    testing sscount0
    Checking sses assesses
    its value 2 is correct!

    >>>test_sscount (p34.sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)

    testing sscount0
    Checking o pneumonoultramicroscopicsilicovolcanoconiosis
    its value 9 is correct!
    '''
    if f == p34.sscount0:
        print ("testing sscount0")
        print ("Checking", args)
        argsBreak = args.find(' ')
        haystack = args [argsBreak+1:]
        needle = args [:argsBreak]
        OGcode = p34.sscount0 (needle, haystack)
        if expected_result == OGcode:
            return print ("its value "+ str(expected_result)+ " is correct!")
        if expected_result != OGcode:
            return print ("its value is not " + str(expected_result)+ " that's incorrect")
        
    if f == p34.sscount1:
        print ("testing sscount1")
        print ("Checking", args)
        argsBreak = args.find(' ')
        haystack = args [argsBreak+1:]
        needle = args [:argsBreak]
        OGcode = p34.sscount1 (needle, haystack)
        if expected_result == OGcode:
            return print ("its value "+ str(expected_result)+ " is correct!")
        if expected_result != OGcode:
            return print ("its value is not " + str(expected_result)+ " that's incorrect") 
    return None

def main ():
    test_sscount (p34.sscount0, 'sses assesses', 2)
    test_sscount (p34.sscount1, 'sses assesses', 2)
    test_sscount (p34.sscount0, 'an trans-Panamanian banana', 6)
    test_sscount (p34.sscount1, 'an trans-Panamanian banana', 6)
    test_sscount (p34.sscount0, 'needle haystack', 0)
    test_sscount (p34.sscount1, 'needle haystack', 0)
    test_sscount (p34.sscount0, '!!! !!!!!', 3)
    test_sscount (p34.sscount1, '!!! !!!!!', 3)
    test_sscount (p34.sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount (p34.sscount1, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount (p34.sscount0, '', 0)
    test_sscount (p34.sscount1, '', 0)
    test_sscount (p34.sscount0, 'a ', 0)
    test_sscount (p34.sscount1, 'a ', 0)
    test_sscount (p34.sscount0, ' abc', 0)
    test_sscount (p34.sscount1, ' abc', 0)
    test_sscount (p34.sscount0, 'a a', 1)
    test_sscount (p34.sscount1, 'a a', 1)

    return None
    
print (main())
