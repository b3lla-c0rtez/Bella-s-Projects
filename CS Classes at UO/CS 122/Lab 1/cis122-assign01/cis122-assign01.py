''' 
CIS 122 Fall 2020 Assignment 1 
Author: Isabella Cortez
Credit: Worked With, Jasmine Wallin
Description: Introduction to programming problem set uses Python numeric data types and 
# operations to solve a variety of small problems. 
'''
#import math library
import math

#
# Question 1
#

print("Question 1")
print("You will be attending a family reunion, and the reunion coordinator wants you to bring watermelon for everyone. The coordinator stated that 250 people will attend the reunion, and 120 of the 250 will be children. The coordinator asks that you plan on two slices of watermelon for each adult, three slices for each child, with 20% extra for those that want more than the planned amounts. Each watermelon on average will produce 15 slices. You need to calculate the total number of watermelons, rounding up to the next highest count of watermelons.")
print("------------------------------------------")

# Calculate the number of watermelons given 120 children at 3 slices,
# 130 adults at 2 slices, 15 slices per watermelon, add 20% extra, rounding up

# Initialize variables with values
adults = 130
children = 120
slices_per_watermelon = 15
extra = 0.2
slices_per_child = 3
slices_per_adult = 2

# Calculate total number of watermelon slices and display number of slices
total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:" , total_slices)

# Add extra amount and display number of slices
total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):" , total_slices)

# Calculate number of watermelons and display number of watermelons
watermelons = total_slices / slices_per_watermelon
print("Total watermelons:" , watermelons)

# Round the number of watermelons and display number of watermelons
watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up):" , watermelons)

#
# Question 2
#

print()
print("Question 2")
print("Your friend was bragging about how many stairs he climbed each day because of his apartment location on the fifth floor. Calculate how many times your friend would have to go down then back up the stairs to reach his fifth floor apartment to reach 100, 500, 1000 and 5000 steps. The apartments all have vaulted ceilings, so use 16 steps per floor in your calculations. Remember to count down and back up as one trip. You will also reuse the variable that contains the target number of steps. Round up.")
print("------------------------------------------")

# Calculate total number of trips given 100, 500, 1000, or 5000 daily steps, 16
# steps per floor, and down and back up the stairs as one trip. Re-use the
# step variable. Round the number of trips up to the nearest whole integer.
# Recommemded variable names: steps_per_floor, target_steps, trips

#Initialize variables
steps_per_floor = 16
floors = 5

# Calculate 100 steps and display number of trips
target_steps_1 = 100
trips = (target_steps_1 / (steps_per_floor * 2))/floors
trips = math.ceil(trips)
trips = print("Trips for 100 steps:" , trips)

# Calculate 500 steps and display number of trips
target_steps_2 = 500
trips = (target_steps_2 / (steps_per_floor * 2))/floors
trips = math.ceil(trips)
trips = print("Trips for 500 steps:" , trips)

# Calculate 1000 steps and display number of trips
target_steps_3 = 1000
trips = (target_steps_3 / (steps_per_floor * 2))/floors
trips = math.ceil(trips)
trips = print("Trips for 1000 steps:" , trips)

# Calculate 5000 steps and display number of trips
target_steps_4 = 5000
trips = (target_steps_4 / (steps_per_floor * 2))/floors
trips = math.ceil(trips)
trips = print("Trips for 5000 steps:" , trips)

#
# Question 3
#

# Calculate total distance walked per week given radius of 90 feet,
# five pivots, two inspections per day, and working 5 days a week. Round
# all results to two decimal places. Use 3.14, or math.pi for the circumference
# equation calculation.

print()
print("Question 3")
print("Your friend worked over the summer on a farm and one of his tasks was to check the irrigation. The farm used a circular stationary irrigation system (also know as center pivot irrigation), and one of your friend's tasks was to walk around and inspect the edge of the irrigation zone. Despite the obvious fitness advantages, your friend thought he'd walked over a hundred miles a week. Did your friend walk over a hundred miles in a single week?")
print("------------------------------------------")

#Initialize variables
radius = 90
pivots = 5
inspections = 2
days_a_week = 5
feet_to_miles = 5280

# Calculate circumference of one pivot
circumference = math.pi * radius * 2

# Calculate and display total distance walked (feet and miles)
total_feet = circumference * days_a_week * pivots * inspections
total_miles = total_feet / feet_to_miles
weekly_distance_feet = round(total_feet, 2)
weekly_distance_miles = round(total_miles, 2)
print("Weekly distance (feet):" , weekly_distance_feet)
print("Weekly distance (miles):" , weekly_distance_miles)




