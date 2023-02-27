def parity(bitrep):

    p = 0

    for bit in bitrep:
        if bit == '1':
            p += 1

    if p % 2 == 0:
        p = '0'
    else:
        p = '1'

    return p
