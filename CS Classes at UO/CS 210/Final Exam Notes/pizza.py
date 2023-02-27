from math import pi

def new_pizza_calculator(diameter, cost):

    r = diameter / 2
    area = pi *r ** 2
    number_of_slices = round(area / 8)
    cost_per_slice = cost / number_of_slices
    cost_per_slice = round(cost_per_slice, 2)
    return cost_per_slice

diameter = 20
my_cost = 30
new_pizza_calculator(diameter, my_cost)

# global namespace = diameter, pi, new_pizza_calculator

def pizza_test(f):
    test_cases = '0', '8', '16'

    for test in test_cases:
        arg1 = test[0]
        arg2 = test[1]

        expected_result = test[2]
        print(f"Checking {f.__name__}('{arg1}, {arg2}')...", end='')

        actual_result = f(arg1,arg2)

        if (actual_result == expected_result):
            print("correct!")
        else:
            print("fail!")

        return None
