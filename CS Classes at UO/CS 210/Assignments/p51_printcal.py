'''
Calendar: printcal.CIS 210 Project 5-1
Author: Isabella Cortez
Credits: Lauren Mathews
prints a calendar
'''

import datetime


def calendar(month, year):
    '''
    int, int -> calendar

    this function takes two ints and
    turns them into calendar. the ints
    reperesent the month and the year
    '''

    day = input('Enter a day: ')

    monthDays = ['31', '28', '31', '30', '31','30', '31', '31', '30', '31', '30', '31']
    monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    adate = datetime.date(year, month, int(day))
    startdate = adate.isoweekday() % 7

    stringMonth = int(month - 1)
    nameOfMonth = monthNames[stringMonth]

    final_day = monthDays[stringMonth]

    month = monthDays[stringMonth]

    days = 'Su Mo Tu We Th Fr Sa'

    next_day = int(day) + 1

    print(f'{month:>2} ', end='')
    print(f'{year:>2} ')
    print(f'{days:>2} ')

    start = '  ' * (startdate)
    print(f'{startdate}', end = '')

    current = 1
    for day in range(8 - startdate):
        print(f'{current:>2} ', end='')
        current += 1
    print()
    for day in range(7):
        print(f'{current:>2} ', end='')
        current += 1
    print()
    for day in range(7):
        print(f'{current:>2} ', end='')
        current += 1
    print()
    for day in range(7):
        print(f'{current:>2} ', end='')
        current += 1
    print()
    while current <= int(month):

        print(f'{current:>2}', end='')
        current += 1
    print()

