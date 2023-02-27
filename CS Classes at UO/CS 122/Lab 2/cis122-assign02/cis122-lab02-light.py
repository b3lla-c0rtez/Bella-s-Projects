''' 
CIS 122 Fall 2020 Lab 2 (Light)
Author: Isabella Cortez
Credit: Lab Class with, Guzman Nateras
Description: Lab 2 Challenge
'''

# Define the function
def avg_light_travel_seconds(distance_miles):

    # Define the speed of light
    speed_of_light = 186282

    # Return the amount of seconds
    return distance_miles / speed_of_light

# Variables to hold the distances
dist_sun_earth = 93000000
dist_sun_pluto = 3670050000

# Testing avg_light_travel_seconds function
time_earth = avg_light_travel_seconds(dist_sun_earth)
time_pluto = avg_light_travel_seconds(dist_sun_pluto)

# Defining the void function to format
def print_results(planetary_object, avg_light_travel_seconds):

    # Light travels from the sun to the Earth/Pluto an average of xxx.
    result_string = "Light travels from the sun to "
    result_string = result_string + planetary_object
    result_string = result_string + " an average of "
    result_string = result_string + str(round(avg_light_travel_seconds))
    result_string = result_string + " seconds. "
    print(result_string)

print_results("the Earth", time_earth)
print_results("Pluto" , time_pluto)
