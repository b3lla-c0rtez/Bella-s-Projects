def my_fun(astring):
    '''
    returns boolean
    '''
    
    symbols = {'@','#','$','%','&','*'}
    symbols_ctr = 0 # assignment

    # c is an identifier
    for c in astring:
        # for and if are keywords
        if c in symbols:
            symbols_ctr += 1 # assignment

    return (symbols_ctr >= 2)
