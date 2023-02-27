def q23(astr):

    countd = {}
    for item in astr:
        if item in countd:
            countd[item] += 1
        else:
            countd[item] = 1

     # countd

    countli = countd.values()
    ct = max(countli)

    mli = [item for item in countd if countd[item] == ct]
    

    return mli
