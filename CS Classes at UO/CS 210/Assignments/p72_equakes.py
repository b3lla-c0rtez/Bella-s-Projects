'''
Data Analysis on Earthquake Data: CIS 210.Project 7-2 Analyzing Earthquakes
Author: Isabella Cortez
Credits: Lauren Matthews, Austin Vierra
takes statistics from earthquake data and calculates different things
'''

import statistics

def equake_readf(fname):
    '''
    (string) -> List

    takes in a string fname that is the file name and reports it
    as a list

    '''
    
    files = open(fname, 'r')

    mag = []

    for line in files:
        mag.append(line.strip())

    return mag
    
def equake_analysis(emags):
    '''
    (list) -> tuple
    
    takes in a list of magnitudes and will dertermine the most
    frequently occuring magnitudes
    '''
    
    countdict = {}

    for item in emags:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1

    countlist = countdict.values()
    maxcount = max(countlist)
    emags = []

    for item in countdict:
        if countdict[item] == maxcount:
            emags.append(item)

    print(emags)
    return emags
    
def equake_report(emags, mmm, minmag):
    '''
    (None, None, None) -> None
    
    reports data gathered from
    emags, mmm, minmag
    '''
    
    mode_mag = statistics.mode(emags)
    print('The mode is: ' , str(emags))

    median_mag = statistics.median(mmm)
    print('The median is: ' , str(mmm))

    mean_mag = statistics.mean(minmag)
    print('The mean is: ' , str(minmag))
    
    return None

def main():
    '''
    ()-> None

    Calls:  equake_readf, equake_analysis, equake_report
    
    Top level function for analysis of earthquake data.
    '''
    
    fname = 'p72_equakes_25f_2019.csv'
    minmag = 2.5

    fname = 'p72_equakes_50f_2019.csv'
    minmag = 5.0

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(emags, mmm, minmag)
    
    return None

    
    
