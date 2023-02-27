''' 
CIS 122 Fall 2020 Assignment 3 Question 3
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews, Jasmine Wallin, Estella Pryor
Description: Create 3 functions that draws 4 snowflakes (one in each quadrant)
'''

import turtle

t = turtle.Turtle()

def draw_line(t, x, y, angle, length):

    """
    Drawing lines using turtle

   first, to draw the line, the pen has to go up, then the setx(x) brings it to the x sport and sety(y) brings it to the y coordinate. The pen goes down and then the angle and length of lines are set. The function starts drawing lines

Args:
   <Each parameter, followed by type, colon, and a description of the paramter>
   e.g.
   t (Turtle): Drawing Turtle
   x (int/float): starting x location
   y (int/float): starting y location)
   angle (int): what degree to turn the pen
   length (int): how long the line is

   Returns:
      None
    """

    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    t.seth(angle)
    t.fd(length)
    
# draw_line(t, 100, 100, 0, 200)
# draw_line(t, -100, - 100, 270, 50)
# draw_line(t, 200, -200, 45, 75)

def draw_radial_lines(t, x, y, length, num_lines):
    
    """
    Drawing a snowflake shape using turtle

   first, to draw the line, the angle is set. then, it draws a certain number of lines and calls the other function in order to draw the different lines. pen is left up

Args:
   <Each parameter, followed by type, colon, and a description of the paramter>
   e.g.
   t (Turtle): Drawing Turtle
   x (int/float): starting x location
   y (int/float): starting y location
   length (int): how long the line is
   num_lines (int): the number of lines there are

   Returns:
      None
    """
    
    angle = 360 / num_lines
    for i in range(num_lines):
        draw_line(t, x, y, i*angle, length)
        
# draw_radial_lines(t, -100, -100, 25, 8)
# draw_radial_lines(t, -100, 100, 100, 4)
# draw_radial_lines(t, 100, -100, 200, 16)
# draw_radial_lines(t, 100, 100, 50, 32)

def draw_radials_in_functions(t, length, num_lines):
    
    """
    Drawing 4 snowflake shape using turtle

   the function draw_radial_lines is called 4 times in order to draw 4 of the shapes. pen is left up 

Args:
   <Each parameter, followed by type, colon, and a description of the paramter>
   e.g.
   t (Turtle): Drawing Turtle
   length (int): how long the line is
   num_lines (int): number of lines for the shapes
   

   Returns:
      None
    """
    
    draw_radial_lines(t, 120, 120, length, num_lines)
    draw_radial_lines(t, -120, 120, length, num_lines)
    draw_radial_lines(t, -120, -120, length, num_lines)
    draw_radial_lines(t, 120, -120, length, num_lines)

draw_radials_in_functions(t, 75, 16)
# draw_radials_in_functions(t, 50, 8)

    
