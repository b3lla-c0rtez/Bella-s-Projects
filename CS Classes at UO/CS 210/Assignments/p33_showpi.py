'''
Show Pi: showpi.CIS 210 Project 3-3 Show Pi Assignment
Author: Isabella Cortez
Credits: Lauren Mathews, Tori Walters, Austin Vierra
create a function that approximates pi, a function that compares pi and the approximate pi value, a function that determines if x and y are in the range, a main driver, and has a function that draws the functions
'''

from turtle import *
import math
import random

def drawBoard():
    '''
    returns none
    draws a board for the showMontePi function
    '''
    
    wn = Screen()
    wn.setworldcoordinates(-2,-2,2,2)

    speed('fastest');
    hideturtle()
    penup()

    color('black')
    goto(-1,0)
    pendown()
    goto(1,0)
    penup()
    goto(0,1)
    pendown()
    goto(0,-1)
    penup()
    goto(0,-1)

    return None

def showMontePi(numDarts):
    '''
    (int) -> float

    calls draw board function to draw the board
    
    takes the number of darts (numDarts) and
    figures out what pi would be
    based on how many are within
    the circle range

    draws blue dots if isInCircle function
    is true and draws red if isInCircle
    function is red

    returns approx value 

    >>>montePi(100)
    3.08
    >>>montePi(100000)
    3.143072
    >>>montePi(10000000)
    3.1418752
    '''
    
    drawBoard()

    inCircle = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        if isInCircle(x, y, 1) == True:
            inCircle += 1
            color('blue')
        else:
            color('red')

        goto(x,y)
        dot()

    approxPi = inCircle/numDarts * 4

    return approxPi

def isInCircle(x, y, r):
    '''
    (int, int, int) -> boolean

    returns truth values for
    whether or not the distance
    is less than or equal to r
    the distance is based on x**2
    + y**2

    returns True or False

    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False 
    '''
    
    d = math.sqrt(x**2 + y**2)
    if d <= r:
        return True
    else:
        return False


def reportPi(num, mypi):
    '''
    (int, int) -> string

    computes the difference
    between value pi and the one
    from showMontePi takes num for
    number of iterations and
    takes mypi compares it to pi

    returns None

    >>> reportPi(1000, mypi)
    With 1000 iterations:
    my approximate value for pi is: 3.104
    math lib pi value is:  3.141592653589793
    This is a 1.2 percent error.
    '''
    
    error = round((abs(showMontePi(num) - math.pi)/math.pi) * 100, 2)
    print("With " + str(num) + " iterations: ")
    print ("my approximate value for pi is: ", str(mypi))
    print ("math lib pi value is: ", str(math.pi))
    print ("This is a", str(error), "percent error.")
    return None

def main():
    '''
    program driver

    calls showMontePi and reportPi
    returnNone
    '''
    k = 1000
    mypi = showMontePi(k)
    reportPi(k, mypi)
    return None

main()
    

        
