''' 
CIS 122 Fall 2020 Assignment 3 Question 2
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews, Jasmine Wallin, Estella Pryor
Description: Create a function with 2 for loops that displays a grid (4 by 4 grid)
'''
def draw_grid(value):

        """
    we are making a 4 by 4 grid using 1, 2, 3, 4

    the first for loop takes the value, which is 4 and prints 4 lines of code. the second for loop prints 1, 2, 3, 4 for the rows

Args:
   value(int): the number of times the loop is being repeated 

Returns:
   None
        """
        
        for i in range(value):
                print()
                for j in range(value):
                        print(j+1, end=' ')
# draw_grid(2)
draw_grid(4)
# draw_grid(10)
