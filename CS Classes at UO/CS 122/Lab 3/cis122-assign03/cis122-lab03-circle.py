''' 
CIS 122 Fall 2020 Lab 3
Author: Isabella Cortez
Credit: Lab Class with, Guzman Nateras
Description: Create 3 functions that draw three concentric circles
'''

import turtle

leo = turtle.Turtle()


def move(tur, x, y):

    '''
    This function moves a turtle object
    Args:
        tur-> a turtle object (turtle)
        x, y, -> the position to move the turtle to (int.)
    '''
     
    tur.pu()
    tur.goto(x, y)
    tur.pd()
    
def draw_circle(tur, radius, x, y):
    
    '''
    This function draws a circle
    Args:
        tur-> is a turtle object to the drawing
        radius -> the raidus of the circle (int)
        x, y, -> the starting point of the circle (int)
    '''
     
    move(tur, x, y-radius)
    tur.circle(radius)

# draw_circle(leo, 50, 0, 0)

# draw_circle(leo, 75, 0, -.25*75)

# draw_circle(leo, 100, 0, -.25*100)

radius = 50
n = 3
x = 0
y = 0
increase = 25

def draw_concentric_circles(n_circles, initial_radius, incremennt, x, y):

    '''
    This function draws concentric circles
    Args:
        n_circles -> the number of the circles to draw (int)
        initial_radius -> the initial size of the first circles radius
        increment -> the amount of pixels to increment the radius 
        x, y, -> the starting position
    '''
     
    for i in range (n):
        draw_circle(leo, initial_radius, x, y)
        initial_radius = initial_radius + increase
draw_concentric_circles(n, radius, increase, x, y)
    
