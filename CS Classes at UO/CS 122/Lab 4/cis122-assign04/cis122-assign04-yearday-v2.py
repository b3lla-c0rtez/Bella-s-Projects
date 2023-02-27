''' 
CIS 122 Fall 2020 Assignment 3 Question 1
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews, Jasmine Wallin, Adam Taba
Description: Create 12 functions that give a calendar date based on the input
'''

import calendar

def is_leap_year(year):
    '''
    This function takes a year and checks if it is a leap year.
    Args:
        year = user inputed year (integer)
    Return:
        returns True and False
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

def valid_year(year):
    '''
    This function checks to make sure the year is not less than 0.
    Args:
        year = user inputed year (integer)
    Return:
        returns True and False
    '''
    if year <= 0:
        print("Errpr, year has to be greater than 0")
        return False
    else:
        return True

def input_year():
    '''
    Takes an user inputed year. It is returned if it is greater than 0 and it does not return the year if it is false.
    Args:
        none
    Return:
        returns year
    '''
    year = int(input("Enter year: "))
    while year <= 0:
        print("Error, day must be greater 0")
        year = int(int("Enter year: "))
    if valid_year(year) is True:
        return year

def valid_month(month):
    '''
    This function takes a month. It will be an error message if the month is less than 0 and greater than 12. 
    Args:
        month = user inputed month/number (integer)
    Return:
        returns True and False
    '''
    if month <= 0:
        print("Error, month must be greater than 0")
        return False
    elif month > 12:
        print("Error, month must be less than or equal 12")
        return False
    else:
        return True

def valid_day_of_year(year, day_of_year):
    '''
    This function makes sure the day of year is good.
    Args:
        year = user inputed year (integer)
        day_of_year = integer; the day of the year
    Return:
        returns True and False
    '''
    if day_of_year > 0:
        return True
    else:
        print("Error, day must be greater than 0")
        return False

def input_day_of_year(year):
    '''
    This function takes the year and returns things based on if it is valid.
    Args:
        year = user inputed year (integer)
    Return:
        returns day and 0
    '''
    day = int(input("Enter day of year: "))
    if is_leap_year(year) is True:
        while day > get_days_in_year(year) or day <= 0:
            while day > get_days_in_year(year):
                print("Error, day must be less than or equal to 366")
            while day <= 0:
                print("Error, day must be greater than 0")
                day = int(input("Enter day of year: "))
        if valid_year(year) and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
    elif is_leap_year(year) is False:
        while day > get_days_in_year(year) or day <=0:
            while day > get_days_in_year(year):
                print("Day must be less than or equal to 365")
                day = int(input("Enter day of year"))
            while day <= 0:
                print("Day must be greater than 0")
                day = int(input("Enter day of year: "))
        if valid_year(year) and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
        else:
            return 0

def get_days_in_year(year):
    '''
    This function checks to make sure the year is a leap year or not.
    Args:
        year = user inputed year (integer)
    Return:
        returns True and False
    '''
    if is_leap_year(year) is True:
        return 366
    elif is_leap_year(year) is False:
        return 365
    else:
        return 0 

def translate_month(month):
    '''
    This function takes a month and returns it based on the number.
    Args:
        month = user inputed month (integer)
    Return:
        returns the 12 months of the year
    '''
    if valid_month(month) is True:
        if month_number == 1:
            return "January"
        elif month_number == 2:
            return "February"
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
            return ""

def get_days_in_month(year, month):
    '''
    This function takes a month and returns it based on the number. It takes into consideration if there is a leap year too. 
    Args:
        year = user inputed year (integer)
        month = user inputed month (integer)
    Return:
        returns the 12 months of the year
    '''
    if month_number == 1:
        return 31
    elif ia_leap_year(year) is True and valid_month(month) is True and month == 2:
        return 29
    elif is_leap_year(year) is False and valid_month(month) is True and month == 2:
        return 28
    elif month_number == 3:
        return 31
    elif month_number == 4:
        return 30
    elif month_number == 5:
        return 31
    elif month_number == 6:
        return 30
    elif month_number == 7:
        return 31
    elif month_number == 8:
        return 31
    elif month_number == 9:
        return 30
    elif month_number == 10:
        return 31
    elif month_number == 11:
        return 30
    elif month_number == 12:
        return 31
    else:
        return 0

def valid_month(year, month, day):
    if valid_year(year) is True and valid_month(month) is True and valid_day_of_year(year, day) is True:
        return True
    else:
        return False

def get_date_string(year, month, day):
    if is_leap_year(year) is True and valid_year(year) is True:
        if 1 <= day <= 31:
            month = "January"
        if 32 <= day <= 60:
            month = "February"
        if 61 <= day <= 91:
            month = "March"
        if 92 <= day <= 121:
            month = "April"
        if 122 <= day <= 152:
            month = "May"
        if 153 <= day <= 182:
            month = "June"
        if 183 <= day <= 213:
            month = "July"
        if 214 <= day <= 244:
            month = "August"
        if 245 <= day <= 274:
            month = "September"
        if 275 <= day <= 305:
            month = "October"
        if 306 <= day <= 335:
            month = "November"
        if 336 <= day <= 366:
            month = "December"
        print(month + " " + str(day) + ", " + str(year))

    if is_leap_year(year) is False and valid_year(year) is False:
        if 1 <= day <= 31:
            month = "January"
        if 32 <= day <= 59:
            month = "February"
            day = day - 31
        if 60 <= day <= 90:
            month = "March"
            day = day - 59
        if 91 <= day <= 120:
            month = "April"
            day = day - 90
        if 121 <= day <= 151:      
            month = "May"
            day = day - 120
        if 152 <= day <= 181:
            month = "June"
            day = day - 151
        if 182 <= day <= 212:
            month = "July"
            day = day - 181
        if 213 <= day <= 243:
            month = "August"
            day = day - 212
        if 244 <= day <= 273:
            month = "September"
            day = day - 243
        if 274 <= day <= 304:
            month = "October"
            day = day - 273
        if 305 <= day <= 334:
            month = "November"
            day = day - 304
        if 335 <= day <= 365:
            month = "December"
            day = day - 334
        print(month + " " + str(day) + ", " + str(year))
            
def start():
    '''
    This function encapsulates all of the code and runs the program.
    Args:
        None
    Return:
        None
    '''
    month = get_date_string
    year = input_year()
    get_date_string(year, month, input_day_of_year(year))

start()

    


