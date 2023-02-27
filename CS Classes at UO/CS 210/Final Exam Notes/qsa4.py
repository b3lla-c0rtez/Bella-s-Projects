def qsa4(f, c):

    with open(f, 'r') as myf:
        for i in range(3):
            myf.readline()

        for nextline in myf:
            nextline = nextline.strip()
            if nextline[0] == c:
                print(nextline)

    return None
