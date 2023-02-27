# import doctest

def myCt(s, c):
    '''
    (str) -> int
    Count number of occurrences of c in string s.
    Return the count (zero is c does not occur in s
    or s is empty string).
    >>> myCt('abbc', 'b')
    2
    >>>myCT('', 'a')
    0
    '''
    ccount = 0
    for ch in s:
        if ch == c:
            ccount += 1
            return ccount
        if ch == 0:
            return 0

# print(doctest.testmod())
