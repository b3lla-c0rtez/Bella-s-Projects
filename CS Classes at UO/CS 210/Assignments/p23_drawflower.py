'''
Flower: Draw Flower.CIS 210 Project 2-3 Flower Assignment
Author: Isabella Cortez
Credits: Austin Vierra, Lauren Mathews
Draw a flower based on the number of squares given and based on the side length and number of sides of a polygon. The main function will call the draw flower function. The draw flower function calls the draw polygon function.
'''

from turtle import *

def drawFlower(numSquares): # function header

    '''
    (int) -> None
    
    main function calls this
    it makes a flower
    you can also call this
    in the shell. it returns
    None
    '''
    
    pencolor('green')
    lt(90)
    fd(50)
    
    for i in range(numSquares):
        pencolor('#DD77FB')
        drawPolygon(25,4)
        rt(360/numSquares)
    return None

def drawPolygon(sideLength, numSides): # function header

    '''
    (int, int) -> None
    
    draw flower calls this
    to draw the polygons
    that are in the flower.
    you can also call this
    in the shell. it returns
    None
    '''
     
    for i in range(numSides):
        fd(sideLength)
        rt(360/numSides)
    return None
        

def main(): # function header
    
    '''
    () -> None
    
    calls the draw
    Flower function.
    this function
    returns None.
    '''
    
    speed(10)
    pensize(2)
    drawFlower(25)
    return None

main()
