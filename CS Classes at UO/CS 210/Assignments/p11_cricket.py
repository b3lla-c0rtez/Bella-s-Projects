'''
Nature's Thermometer: Cricket Chirps.CIS 210 Project 1-1 Hello-Cricket
Author: Isabella Cortez
Credits: N/A
Determine the temperature based on cricketchirps. (Farmers Almanac)
'''

def chirps_to_ctemp(ch25): #FUNCTION HEADER
    '''
    (int) -> float
                        #Brief Description
                        #Params, return value
    Return celcius temp estimaated based on
    number of cricket chirps in a 25 second
    interval (ch 25) - divide by 3 and add 4
    to get the celsius temperature
                           #EXAMPLES OF USE
    >>> chirps_to_ctemp(48)
    20.0
    >>> chirps_to_ctemp(93)
    35.0
    >>> chirps_to_ctemp(0)
    4.0
    '''
    ctemp = ((ch25 / 3) + 4)
    print(ctemp)

def chirps_to_ftemp(ch14):
    '''
    (int) -> int
                        #Brief Description
                        #Params, return value
    Return fahrenheit temp estimated based on
    number of cricket chirps in a 14 second
    interval (ch14) - add 40. The estimated
    temperature is returned.

    >>> chirps_to_ftemp(0)
    40
     >>> chirps_to_ftemp(50)
    90
    '''
    ftemp = (ch14 + 40)
    print(ftemp)
    
