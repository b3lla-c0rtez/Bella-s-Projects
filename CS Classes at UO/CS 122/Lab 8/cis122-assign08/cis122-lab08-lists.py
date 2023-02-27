''' 
CIS 122 Fall 2020 Lab 8
Author: Isabella Cortez
Credit: Lab Class
Description: Generates integers, sorts the integers, and prints out the range 
'''

import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    '''
    description: this function creates a list with random integer numbers
    args:
    num = the number of elements in the range
    start = the lower bound of the range
    end = the upper bound of the range
    sort = whether to sort the list
    Return:
        t = the resulting list
    '''
    # creating empty list
    t = []
    # check if num is lower or equal to 0
    if num <= 0:
        print("num must be > 0")
    # check that num is an integer
    elif not isinstance(num, int):
        print("num must be an integer")
    # check that both start and end are integers
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print("start_range and end_range must be integers")
    else:
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)

    if sort_list.upper() == 'Y':
        t.sort()
    return t

def get_high_score(lst_param):
    '''
    description: this function shows the high score of the random integers in the list
    args:
        lst_param (int) = the stuff inside the list
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list
        0 = if nothing is entered
        copy[-1] = the high score
    '''
    if not isinstance(lst_param, list):
        print("list argument expected")
        return -1
    elif len(lst_param) == 0:
        return 0
    else:
        copy = lst[:]
        copy.sort()
        return copy[-1]

def get_low_score(lst_param):
    '''
    description: this function shows the low score of the random integers in the list
    args:
        lst_param (int) = the stuff inside the list
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list
        0 = if nothing is entered
        copy[0] = the low score
    '''
    if not isinstance(lst_param, list):
        print("list argument expected")
        return -1
    elif len(lst_param) == 0:
        return 0
    else:
        copy = list[:]
        copy.sort()
        return copy[0]
    
def get_mean_score(lst_param):
    '''
    description: this function shows the mean of the random integers in the list
    args:
        lst_param (int) = the stuff inside the list
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list
        0 = if nothing is entered
        sum(lst_param)/len(lst_param) = the mean
    '''
    if not isinstance(lst_param, list):
        print("list argument expected")
        return -1
    elif len(lst_param) == 0:
        return 0
    else:
        return sum(lst_param)/len(lst_param)

def get_median_score(lst_param):
    '''
    description: this function shows the mean of the random integers in the list
    args:
        lst_param (int) = the stuff inside the list
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list
        0 = if nothing is entered
        lst_param[0] = if list is 1
        copy[index] = returns the sorted index/sorted list if the list parameter mod 2 is equal to 1/has a remainder of 1
        (elem1 + elem2) / 2 = the median
    '''
    if not isinstance(lst_param, list):
        print("List argument expected")
        return -1
    elif len(lst_param) == 0:
        return 0
    elif len(lst_param) == 1:
        return lst_param[0]
    elif len(lst_param) % 2 == 1:
        copy = lst_param[:]
        copy.sort()
        index = len(copy) // 2
        return copy[index]
    else:
        copy = lst_param[:]
        copy.sort()
        index1 = len(copy) // 2
        index2 = index1 - 1
        elem1 = copy[index1]
        elem2 = copy[index2]
        return (elem1 + elem2) / 2

def count_range(lst_param, low_score, high_score):
    '''
    description: this function counts the range of values
    args:
        lst_param (int) = the stuff inside the list
        low_score (int) = the low score
        high_score (int) = the high score
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list and low score has to be < high score and the numbers have to be integers
        0 = if list parameter is 0
        copy[index] = returns the sorted index/sorted list if the list parameter mod 2 is equal to 1/has a remainder of 1
        counter = 
    '''
    if not isinstance(lst_param, list):
        print("List argument expected")
        return -1
    elif len(lst_param) == 0:
        return 0
    elif not isinstance(low_score, int) or not isinstance(high_score, int ):
        print("start and end must be integers")
        return -1
    elif low_score >= high_score:
        print("start must be < end")
        return -1
    else:
        counter = 0
        for elem in lst_param:
            if low_score <= elem <= high_score:
                counter += 1
        return counter

def list_range(lst_param):
    '''
    description: this function shows the range of values from the list
    args:
        lst_param (int) = the stuff inside the list
    Return:
        -1 = something has to be entered for it to work and it has to be inside the list
    '''
    if not isinstance(lst_param, list):
        print("List argument expected")
        return -1
    else:
        counter_a = count_range(lst_param, 90, 100)
        counter_b = count_range(lst_param, 80, 89)
        counter_c = count_range(lst_param, 70, 79)
        counter_d = count_range(lst_param, 60, 69)
        counter_f = count_range(lst_param, 0, 59)
        print("A -" , counter_a)
        print("B -" , counter_b)
        print("C -" , counter_c)
        print("D -" , counter_d)
        print("F -" , counter_f)
