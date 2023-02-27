def who_is_winning(fname):
    '''
    (str) -> str

    this function takes in a file name (westcoast_covid).
    it determines which state has administered the most
    vaccines.
    
    >>>who_is_winning('westcoast_covid')
    Washington is winning.
    '''
    with open(fname, 'r') as COVID:
        COVID.readline()
        COVID.readline()
        COVIDli = []

        for item in COVID:
            item = item.strip().split()
            COVID.append(item[0])

    return COVID
 
