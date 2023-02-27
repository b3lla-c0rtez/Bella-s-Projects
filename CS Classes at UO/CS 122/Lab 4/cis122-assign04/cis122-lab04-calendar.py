''' 
CIS 122 Fall 2020 Assignment 3 Question 1
Author: Isabella Cortez
Credit: Lab Class
Description: Creates a calendar using some functions
'''

def get_full_month(month_number):
    '''
    This function receives a number between 1-12 and returns the corresponding month
    Args:
        month_number -> an integer between 1-12

    Returns:
        string of the corresponding month name
    '''
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "Febuary"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    else:
        print("Number must be an integer between 1 and 12 " + str(month_number) + " is invalid")
        return ' '
    
print(get_full_month(2))
# Feburary
print(get_full_month(13))
# ''

def test_get_full_month():
    '''
    Tests to see if month works
    Args:
        None

    Returns:
        None
    '''
    for i in range(14):
        month = get_full_month(i)
        print(i, month)
# test_get_full_month()

def is_leap_year(year):
    '''
    Tests to see if it is a leap year
    Args:
        year -> integer; value for year
    Returns:
        returns true or false
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2000))
# true
print(is_leap_year(1800))
# false
print(is_leap_year(1997))
# false

def test_is_leap_year(start_year, end_year):
    '''
    This function receives a number between 1-12 and returns the corresponding month
    Args:
        month_number -> an integer between 1-12

    Returns:
        string of the corresponding month name
    '''
    for year in range(start_year, end_year):
        if is_leap_year(year):
            print(year)
            
import calendar

def validate_is_leap_year(start_year, end_year):
    '''
    This function receives a number between 1-12 and returns the corresponding month
    Args:
        month_number -> an integer between 1-12

    Returns:
        None
    '''
    counter = 0
    for year in range(start_year, end_year):
        my_result = is_leap_year(year)
        calendar_result = calendar.isleap(year)

        if my_result != calendar_result:
            counter = counter + 1
            print(year)

    if counter == 0:
        print("No mismatches found")

validate_is_leap_year(1996, 2112)

