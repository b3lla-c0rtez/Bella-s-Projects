'''
File Concordance: CIS 210.Project 7-4 Concordance for File Name
Author: Isabella Cortez
Credits: Lauren Matthews, Austin Vierra
Returns a concordance for a file
'''

def fconcordance(fname):
    ''' (string) -> None
    creates a list of the frequerncy words occur
    in a text file
    '''
    
    text = open(fname, "r")
    d = dict() 
  
    for line in text: 
        line = line.strip() 

        line = line.lower() 
  

        words = line.split(" ") 
  
        for word in words: 
            if word in d: 
                d[word] = d[word] + 1
            else: 
                d[word] = 1
  
    for key in list(d.keys()): 
        print(key, "occurs in", d[key], 'lines')
