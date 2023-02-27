'''
Algorthims: Python Variations.CIS 210 Project 1-2 Variations
Author: Isabella Cortez
Credits: Lauren Mathews, Tori Walters, Austin Vierra
Practice writing Python code for CIS 210 with functions that have different algorithms.
'''

def convert(i, j, k): # function header
    
    '''
    (int) -> int
                        #Brief Description
                        #Params, return value
    Return a whole number when you input
    3 individual numbers. The numbers
    should be in the 1s, 10s, and 100s place.
    Then the numbers have to be added and it
    on the value of i, j, and k.
                           #EXAMPLES OF USE
    >>> convert(1,2,3)
    321
    >>> convert(0,0,1)
    100
    >>> convert(1,0,0)
    1
    >>> convert(0,0,0)
    0
    '''
    
    nums = k, j, i
    first = k * 100
    second = j * 10
    third = i * 1
    solution = first + second + third
    if k == 0:
        solution = second + third
        if j == 0:
            solution = third
            return solution
            if i == 0:
                solution = 0
                return solution
        elif j != 0:
            return solution
    return solution

    
def add_digits(n): # function header
    
     '''
    (int) -> int
                        #Brief Description
                        #Params, return value
    Return the sum of a 3-digit integer.
    The function takes a parameter that has
    3 digits and adds each individual digit. 
                           #EXAMPLES OF USE
    >>> add_digits(789)
    24
    >>> add_digits(101)
    2
    '''
     
    digit1 = n //100 # 7
    get100 = digit1 * 100 #700
    get10 = n - get100 # 89
    digit2 = get10 // 10 # 8
    get1 = digit2 * 10 # 80
    digit3 = n - (get100 + get1)
    answer = digit1 + digit2 + digit3
    return answer

def add_digits2(nums): # function header
    
    '''
    (int) -> int
                        #Brief Description
                        #Params, return value
    Return the sum of an integer with any
    number of digits. The function takes a
    parameter that is an integer and adds
    each individual digit of it. 
                           #EXAMPLES OF USE
    >>> add_digits2(789)
    24
    >>> add_digits2(101)
    2
    >>> add_digits2(000)
    0
    >>> add_digits2(5)
    5
    >>> add_digits2(10101)
    3
    '''
    
    answer = 0
    while nums > 0:
        counter = nums % 10
        nums = nums // 10
        answer = answer + counter
        
    return(answer)
        
def profit(audience): # function header
    
    '''
    (int) -> float
                        #Brief Description
                        #Params, return value
    Returns the profit a theater makes. The
    function takes a parameter which is the
    number of audience members/attendees
    at the show. Using the cost of the ticket
    (5), the cost of the performance (20) and
    the attendee (.50), the function calculates
    the profit the theater makes.
                           #EXAMPLES OF USE
    >>> profit(5)
    2.5
    >>> profit(10)
    25.0
    >>> profit(0)
    -20.0
    >>> profit(1)
    -15.5
    '''
    
    earn = audience * 5
    performance_cost = 20
    attendee = audience * .5
    answer = earn - (performance_cost + attendee)
    return answer
    
