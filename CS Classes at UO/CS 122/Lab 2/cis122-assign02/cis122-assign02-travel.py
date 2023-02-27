''' 
CIS 122 Fall 2020 Assingment 2 Question 3
Author: Isabella Cortez
Credit: Tori Walters, Lauren Matthews
Description: Create two functions to display travel time in hours, minutes, and seconds
'''

import math

# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time (distance, speed):

    # Defined Variables
    hours = int(distance / speed)
    minutes = int(((distance / speed) - hours)*60)
    
    # Return travel time in minutes
    return minutes


# Output travel time hours, minutes, and seconds given distance and speed
def print_travel_time (distance, speed):

        # Variables
        hours = int(distance/speed)
        minutes =(((distance/speed)-hours)*60)
        seconds = round((minutes % 1)*60)

        # Result string
        resultString = 'To travel ' + str(distance) + ' miles at ' + str(speed) + ' MPH will take ' + str(int(hours)) + ' hr, ' + str(calc_travel_time(distance,speed)) + ' min and ' + str(seconds) + ' seconds'    

    # Print travel time
        print(resultString)

print_travel_time(120, 55)
print_travel_time(120, 70)
print_travel_time(5, 25)
print_travel_time(5, 35)

