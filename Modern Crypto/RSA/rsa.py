# all parameters must be passed in str and return int

from gcd_calculator import gcd
from inverse import inverseMod


def rsa(mode, plainText, cipherText, p, q, n, phi_n, e, d):
    if mode == 'p':
        if n != 'nan' and q != 'nan':
            return int(n) / int(q)
        print('case not included')
    if mode == 'q':
        if n != 'nan' and p != 'nan':
            return int(n) / int(p)
        print('case not included')
    if mode == 'n':
        if p != 'nan' and q != 'nan':
            return int(p) * int(q)
        print('case not included')
    if mode == 'phi_n':
        if p != 'nan' and q != 'nan':
            return (int(p) - 1) * (int(q) - 1)
        if n != 'nan' and (p != 'nan' or q != 'nan'):
            if p != 'nan':
                return (int(p) - 1) * (int(n) / int(p) - 1)
            return (int(q) - 1) * (int(n) / int(q) - 1)
        print('case not included')
    if mode == 'enc':
        if plainText != 'nan' and e != 'nan' and n != 'nan':
            return pow(int(plainText), int(e), int(n))
        print('case not included')
    if mode == 'dec':
        if cipherText != 'nan' and d != 'nan' and n != 'nan':
            return pow(int(cipherText), int(d), int(n))
        print('case not included')
    if mode == 'inverse':
        if e != 'nan' and n != 'nan':
            return inverseMod(e, n)
        if e != 'nan' and p != 'nan' and q != 'nan':
            return inverseMod(e, int(p) * int(q))
        if d != 'nan' and n != 'nan':
            return inverseMod(d, n)
        if d != 'nan' and p != 'nan' and q != 'nan':
            return inverseMod(d, int(p) * int(q))
        print('case not included')


while True:
    mode = input('mode: ')
    plainText = input('plaintext: ')
    cipherText = input('ciphertext: ')
    p = input('p: ')
    q = input('q: ')
    n = input('n: ')
    phi_n = input('phi_n: ')
    e = input('e: ')
    d = input('d: ')
    print(str(rsa(mode, plainText, cipherText, p, q, n, phi_n, e, d)) + '\n')
