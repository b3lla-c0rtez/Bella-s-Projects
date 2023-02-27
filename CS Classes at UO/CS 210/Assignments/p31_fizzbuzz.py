'''
Make Fizzbuzz Game: Fizzbuzz.CIS 210 Project 3-1 Fizzbuzz Assignment
Author: Isabella Cortez
Credits: Lauren Mathews
create a the fizzbuzz game by using a for loop and counter. print out numbers and if it is divisible by 3 print fizz, by 5 print buzz, by both 3 and 5, print fizzbuzz
'''

def fb(n):
    '''
    (int) -> int and string

    n = number to count to

    print numbers 1-n, if the counter
    number is divisible by 3, print fuzz,
    if the counter number is divisible by
    5, print 5, if it is divisible by both
    3 and 5, print fizzbuzz

    returns None
    
    >>>fb(5)
    1
    2
    fizz
    3
    4
    buzz
    Game over!
    '''
    
    counter = 0
    for i in range(n):
        while counter < n:
            counter += 1
            if counter % 3 == 0:
                print("fizz")
            elif counter % 5 == 0:
                print("buzz")
            else:
                print(counter)
            if ((counter % 3 == 0) and (counter % 5 == 0)):
                print("fizzbuzz")
        
    print("Game over!")
    return None

def fizzbuzz(n):
    for i in range(1, n+1):
        m3 = (i % 3) == 0
        m5 = (i % 5) == 0

        if m3 and m5:
            print('fizzbuzz')
        elif m3:
            print('fizz')
        elif m5:
            print('buzz')
        else:
            print(i)
    print('Game over!')

    return
