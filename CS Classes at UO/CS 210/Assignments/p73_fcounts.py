'''
File Counting: CIS 210.Project 7-3 File Processing
Author: Isabella Cortez
Credits: Lauren Matthews, Austin Vierra
counts number of lines, characters, and words in txt file
'''

def fcounts (fname):
    '''
    (string) -> List

    takes in a string fname that is the file name and reports it
    as a list and reports the number of words
    '''
    
    with open(fname, 'r') as inFile:

        lineCount = 0
        wordCount = 0
        charCount = 0
        words = []
        
        for aLine in inFile:
            lineCount += 1
            charCount = charCount + len(aLine[0:-1])
            word = aLine.split()
            words += word
            
            if word in words:
                wordCount = 1
            else:
                wordCount += 1
                
    
        print('The number of lines in file', fname, 'is:', lineCount)
        print('The number of characters in file', fname, 'is:', charCount)
        print('ITEM FREQUENCY')
        print(words, wordCount)
       
def main():
    '''
    ()-> None

    Calls:  fcounts
    '''
    fname = 'tinyf.txt'
    fcounts(fname)

    
main()
