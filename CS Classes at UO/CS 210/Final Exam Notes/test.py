

total = 0
astr = "a b c d e f"
i = 0
while i < len(str(astr)):
    if astr[i] == ' ':
        total += 1
        i += 1
print(total)
'''
def my_fun(astring):
    symbol = '#'
    symbols_ctr = 0

    for c in astring:
        if c == symbol:
            symbols_ctr += 1
    return (symbols_ctr >= 2)
'''

import math
def myDist(x, y):
    '''
    (int, int) -> float

    This function takes two parameters, x and y
    and calculates the between them and the
    origin (0,0). It returns the distance

    >>>myDist(2,2)
    2.8284271247461903
    
    >>>myDist(6,7)
    9.219544457292887
    '''
    
    origin_x = 0
    origin_y = 0
    distance = math.sqrt((((x - origin_x)**2) + ((y - origin_y)**2)))
    return distance

def isIn(x, y, r):
    '''
    (int, int, int) -> None

    This function takes three parameters, x, y, and r
    and determines whether the distance between them (x and y)
    is inside a circle with a radius r.

    >>>myDist(2,2,3)
    This point is inside a circle of radius: r
    
    >>>myDist(6,7,3)
    This point is not inside a circle of radius: r
    '''
    
    myDist(x,y)
    d = math.sqrt((((x - 0)**2) + ((y - 0)**2)))
    if d <= r:
        print('This point is inside a circle of radius: ' , str(r))
    else:
        print('This point is not inside a circle of radius: ' , str(r))
    return None
