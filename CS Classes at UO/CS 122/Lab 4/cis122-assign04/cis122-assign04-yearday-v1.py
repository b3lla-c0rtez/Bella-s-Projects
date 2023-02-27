''' 
CIS 122 Fall 2020 Assignment 3 Question 1
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews, Jasmine Wallin
Description: Creates a function that makes a calendar
'''

import calendar

month = " "

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
                    if day_given <= 0:
                        month = "error, number has to be greater than 0"
                    elif 1 <= day_given <= 30:
                        month = "January"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 31 <= day_given <= 59:
                        month = "Feburary"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 60 <= day_given <= 90:
                        month = "March"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 91 <= day_given <= 121:
                        month = "April"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 122 <= day_given <= 151:
                        month = "May"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 152 <= day_given <= 181:
                        month = "June"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 182 <= day_given <= 212:
                        month = "July"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 213 <= day_given <= 242:
                        month = "August"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 243 <= day_given <= 273:
                        month = "September"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 274 <= day_given <= 303:
                        month = "October"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 304 <= day_given <= 335:
                        month = "November"
                        month = month + " " + str(day_given) + ", " + str(year)
                    elif 336 <= day_given <= 366:
                        month = "December"
                        month = month + " " + str(day_given) + ", " + str(year)
                    else:
                        month = "error, number has to be less than or equal to 366"
                    
            else:
                if day_given <= 0:
                    month = "error, number is greater than 0"
                elif 1 <= day_given <= 30:
                    month = "January"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 31 <= day_given <= 58:
                    month = "Feburary"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 59 <= day_given <= 89:
                    month = "March"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 90 <= day_given <= 119:
                    month = "April"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 120 <= day_given <= 150:
                    month = "May"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 151 <= day_given <= 180:
                    month = "June"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 181 <= day_given <= 211:
                    month = "July"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 212 <= day_given <= 241:
                    month = "August"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 242 <= day_given <= 272:
                    month = "September"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 273 <= day_given <= 302:
                    month = "October"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 303 <= day_given <= 334:
                    month = "November"
                    month = month + " " + str(day_given) + ", " + str(year)
                elif 335 <= day_given <= 365:
                    month = "December"
                    month = month + " " + str(day_given) + ", " + str(year)
                else:
                    month = "error, number has to be less than or equal to 365"
                    
        else:
            if day_given <= 0:
                month = "error, number has to be greater than 0"
            elif 1 <= day_given <= 30:
                month = "January"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 31 <= day_given <= 59:
                month = "Feburary"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 60 <= day_given <= 90:
                month = "March"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 91 <= day_given <= 121:
                month = "April"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 122 <= day_given <= 151:
                month = "May"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 152 <= day_given <= 181:
                month = "June"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 182 <= day_given <= 212:
                month = "July"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 213 <= day_given <= 242:
                month = "August"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 243 <= day_given <= 273:
                month = "September"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 274 <= day_given <= 303:
                month = "October"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 304 <= day_given <= 335:
                month = "November"
                month = month + " " + str(day_given) + ", " + str(year)
            elif 336 <= day_given <= 366:
                month = "December"
                month = month + " " + str(day_given) + ", " + str(year)
            else:
                month = "error, number has to be less than or equal to 366"
    else:
        if day_given <= 0:
            month = "error, number is greater than 0"
        elif 1 <= day_given <= 30:
            month = "January"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 31 <= day_given <= 58:
            month = "Feburary"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 59 <= day_given <= 89:
            month = "March"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 90 <= day_given <= 119:
            month = "April"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 120 <= day_given <= 150:
            month = "May"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 151 <= day_given <= 180:
            month = "June"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 181 <= day_given <= 211:
            month = "July"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 212 <= day_given <= 241:
            month = "August"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 242 <= day_given <= 272:
            month = "September"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 273 <= day_given <= 302:
            month = "October"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 303 <= day_given <= 334:
            month = "November"
            month = month + " " + str(day_given) + ", " + str(year)
        elif 335 <= day_given <= 365:
            month = "December"
            month = month + " " + str(day_given) + ", " + str(year)
        else:
            month = "error, number has to be less than or equal to 365"
    return month
        
    
year = input("Enter year: ")
day_given = input("Enter day of year: ")
year = int(year)
day_given = int(day_given)

print(is_leap_year(year))
