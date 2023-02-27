def lowtemps(f):
    '''
    (str) -> dict
    '''

    with open(f) as tempf:
        tempf.readline()
        my_temps = tempf.readline().strip().split(',')

        tempd = {}
        day = 1

        for temp in my_temps:
            tempd[day] = int(temp)
            day += 1

        return tempd
