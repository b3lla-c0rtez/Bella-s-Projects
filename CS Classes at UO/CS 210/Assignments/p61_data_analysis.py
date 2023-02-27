'''
Data Analysis: CIS 210.Project 6-2 Analyzing Data
Author: Isabella Cortez
Credits: Isabella Cortez
takes statistics from earthquake values and caculates things
'''
import statistics

equakes = ([5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9,
           2.5, 4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3,
           3.1, 4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9,
           5.0, 2.5, 3.2, 2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6,
           2.9, 2.7, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1, 2.5,
           4.4, 4.6, 5.7, 4.5, 4.7, 5.1, 2.9, 3.3, 2.7, 2.8,
           2.9, 2.6, 5.3, 6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
           2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0, 2.5,4.9, 4.9,
           2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5, 5.0, 4.8,
           2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7, 2.9,
           2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8,
           4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5,
           4.5, 2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5,
           4.6, 2.6, 5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
           3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4,
           4.2, 3.1, 2.8, 4.5, 2.9, 3.1, 4.3, 4.9, 5.2, 2.6,
           6.7, 2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6, 2.5, 3.2,
           2.7, 6.2, 4.0, 4.6, 4.9, 2.5, 5.1,3.3, 2.5, 4.7,
           2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3])


def mean(equakes):
    '''
    float -> (float)

    this function takes in the earthquake measurements
    and calculates the mean
    '''
    meanEquakes = statistics.mean(equakes)

    return meanEquakes

def median(equakes):
    '''
    float -> (float)

    this function calculates the median of the
    earthquake measurements
    '''
    medianEquakes = statistics.median(equakes)

    isEven(medianEquakes)

    return medianEquakes

def mode(equakes):
    '''
    float -> (float)

    this function takes in the earthquake measurements
    and calculates the mode
    '''
    modeEquakes = statistics.multimode(equakes)

    return modeEquakes

def isEven(n):
    '''
    float -> (float)

    this function takes in the earthquake measurements
    and determines which are even or not
    '''

    num = n % 2

    if num > 0:
        return True
    else:
        return False

def frequencyTable(equakes):
    '''
    float -> (float)

    this function takes in the earthquake measurements
    and figures out the frequency of the earthquakes
    '''

    countDict = {}

    for item in equakes:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    itemList = list(countDict.keys())
    itemList.sort()

    print('ITEM', 'FREQUENCY')

    for item in itemList:
        print(item, '   ', countDict[item])


def main():
    '''
    driver program
prints sentences
    '''
    print('The mean is:', mean(equakes))
    print('The median is:', median(equakes))
    print('The mode is:', mode(equakes))
    frequencyTable(equakes)
    return None

main()
