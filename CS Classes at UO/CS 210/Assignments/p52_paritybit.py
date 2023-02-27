def parity (bitrep):
    one_cnt = 0
    for letters in bitrep:
        if letters == '1':
            one_cnt += 1
    if (one_cnt % 2) != 0:
        return '1'
    if (one_cnt % 2) == 0:
        return '0'
    
def encode (letter):
    binary = ('{0:b}'.format(ord(letter)))
    bit_parity= parity (binary)
    result = bit_parity + binary
    return result

def decode (pletter):
    if parity(pletter) == '0':
        
        binary_string = int(pletter[1:],2)
        result = chr(binary_string)
    else:
        result = '*'
    return result


def main ():
    word = 'cat'
    for letter in word:
        print(decode(encode(letter)), end='')

    return None
