'''
Data Analysis on Majors: CIS 210.Project 7-1 Analyzing Majors
Author: Isabella Cortez
Credits: Lauren Matthews, Austin Vierra
takes statistics from list of majors and calculates different things
'''

def majors_readf (fname):
    ''' (string) -> List

    takes in a string fname that is the file name and reports it
    as a list

    ''''
    file = open(fname,'r')
    majorslist =[ ]
    for line in file:
        majorslist.append(line.strip())

    return majorslist

def major_analysis(majorsli):
    ''' (list) -> tuple
    takes in a list of major and will dertermine the most
    frequently occuring majors
    '''
    countdict = {}

    for item in majorsli:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1

    
    
    
    countlist = countdict.values()
    maxcount = max(countlist)
    modelist= []

    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist
        

def majors_report(majors_mode, majors_ct, majorsli):
    '''  (None, None, None) -> None
    reports data gathered from
    majors_mode, majors_ct, majorsli
    '''
    
    print('Mode of data is:', majors_mode)
    print('Total number of majors:', majors_ct)

def main():
     '''()-> None

    Calls:  majors_readf, majors_analysis, majors_report
    
    Top level function for analysis of CIS 210 majors data.
    '''
     
    fname = 'p71-majors-cis210W20.txt'
    majorsli = majors_readf(fname)
    majors_mode, majors_ct = major_analysis(majorsli)
    majors_report(majors_mode, majors_ct, majorsli)
    return None

main()  
