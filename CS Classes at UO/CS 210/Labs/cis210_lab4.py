def hello(s):
    ''' '''
    print('Hello, ' + s + '.')
    return None

def ciao(s):
    ''' '''
    print('Ciao, ' + s + '.')
    return None

def greeting(f, s):
    ''' '''
    if f == hello:
        print("Calling hello")
        hello(s)
    else:
        print("Calling ciao")
        ciao(s)

    return None
