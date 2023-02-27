''' 
CIS 122 Fall 2020 Lab 5
Author: Isabella Cortez
Credit: Lab Class with, Guzman Nateras
Description: Creates a function that determines the factorial
'''

import math

def factorial(num):
    '''
    This function commputes the factorial of a number
    Args:
        num -> the number of which we coompute the factorial
    Returns:
        the factorial
    '''
    # Convert number to integer
    integer_num = int(num)
    print("int num = " , integer_num)

    # If number < 0 print error and return None
    if integer_num < 0:
        print("Error: in valid input " + str(integer_num))
        return None
    # If number == 0 return 1
    elif integer_num == 0:
        return 1
    # If number > 0
    else:
        # Initialize total to 1
        total = 1
        # Loop from 1 to number
        for var in range(1, integer_num + 1):
            # total = total * loop value
            total *= var
        # Return total
        return total

# print(factorial(4.3))

def test_factorial(num, show = False):
    errors = 0
    range_num = num + 1
    for i in range(range_num):
        my_results = factorial(i)
        math_results = math.factorial(i)

        if show == True:
            print(i, ":" ,my_results, math_results)
        
        if my_results != math_results:
            errors += 1
            print("*" + str(my_results) + " " + str(math_results))

    print("Errors (" + str(num) + "):" , errors)

n = int(input("Enter factorial number: " ))
print(factorial(n))
# test_factorial(10)
        

