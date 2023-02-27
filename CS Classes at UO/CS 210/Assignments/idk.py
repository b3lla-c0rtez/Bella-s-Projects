def twice(n):
    return 2*n

def thrice(n):
    n = 10
    return twice(n) + n

def main():
    i = 5
    result = thrice(i)
    print("Result is", result)
    return
main()

def qred(n):
    r = 1
    for i in range(n):
        r = r*2
    print(r)
    return

def hello():
    total = 0
    astr = 'a b c d e f'
    i = 1
    while i < len(astr):
        if astr[i] == '':
            total += 1
        i += 1
    print(total)

hello()

def qblue(x):
    count = 0
    while x > 0:
        count += 1
        x = x // 10
    return count

def qgold_aux(st, v, c):
    vstr = ''
    cstr = ''

    for ch in st:
        if ch in v:
            vstr += ch
        if ch in c:
            cstr += ch

    return len(cstr) < len(vstr)

def qgold():
    VOWELS = 'AEIOU'
    CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'

    print(qgold_aux('CIS 210', VOWELS, CONSONANTS))
    return

qgold()

def example():
    with open('file_example.txt', 'r') as checkf:
        interesting_data = checkf.readline()
    print(interesting_data)

def foo(x):
    x.pop
    return

def bar(x):
    foo(x)
    y = foo(x); print(x, y)
    x = foo(x)
    return

def myD_to_li(myD):
    list1 = []
    list2 = []
    for key in myD:
        list1.append(key)
        list2.append(myD[key])
        return (list1, list2)

              
