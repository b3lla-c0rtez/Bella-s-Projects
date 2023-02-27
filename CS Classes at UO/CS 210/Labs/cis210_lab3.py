import math

def pizza_calculator(diameter, cost):

    a = circle_area(diameter)
    cost_per_inch = cost / a
    cost_per_inch = round(cost_per_inch, 3)
    print ("diameter = " , diameter)
    print("cost = " , cost)
    print ("d = " , diameter)
    print("c = " , cost)
    return cost_per_inch

def circle_area(diameter):
    r = diameter / 2
    area = math.pi * r ** 2
    print("r = " , r)
    print("area =" , area)
    return area


def main():
    print("Pizza 1: " , pizza_calculator(14, 18))
    print('')
    print("Pizza 2: " , pizza_calculator(14, 20.25))
    print('')
    print("Pizza 3: " , pizza_calculator(20, 27))

    return None

main()


def is_even(n):
    return n % 2 == 0

def perror(msg, line):
    print( "Error: (line " , line , ") " , msg)
    return None
