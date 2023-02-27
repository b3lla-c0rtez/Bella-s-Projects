'''
CIS 210 racetrack, 2021 Final Question 22

Author: Isabella Cortez

Credits: N/A

This program reads a textfile and draws a racetrack based on the data
'''
from turtle import *

def racetrack(f):
    
    '''
    (str) -> None

    Create a function that reads a textfile (racetrack_gps.txt)
    and returns None. The function should plot the animation of
    the user going around the track based on the longitude of the
    and latititude of the GPS.

    >>> readFile('racecar_gps.txt')
    (longitudes, latitudes, and logs for GPS//textfile data)
    None
    shows picture of racetrack
    '''
    
    with open(f, 'r') as rc:
        racecar = {}
        key = 0
        rc.readline()
        
        #move past header
        for line in rc:
            line = line.strip().split(',')
            latitude = float(line[1])
            longitude = float(line[2])
            key += 1
            racecar[key] = [longitude, latitude]

        speed('fastest')
        wFact = (10)
        hFact = (10)
        hideturtle()
        penup()
        # note: len colorlist must be >= k
        colorlist = ['red', 'green', 'blue', 'orange', 'yellow', 'purple','cyan', 'black', 'brown', 'silver']
        tracer(0,0)
        for cluster in range(k):
            color(colorlist[cluster])
            for keys in rcClusters[cluster]:
                longitude = rcqDict[keys][0]
                latitude = rcDict[keys][1]
                goto(longitude*wFact, latitude*hFact)
                dots = 5
                dot(dots)
                update()
                exitonclick()
        return None
