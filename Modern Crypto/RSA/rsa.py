# all parameters must be passed as str and return as str

from inverse import inverseMod


def rsa(mode, plainText, cipherText, p, q, n, phi_n, e, d):
    if mode == 'p':
        if n != '' and q != '':
            return str(int(n) / int(q))
        return ''
    if mode == 'q':
        if n != '' and p != '':
            return str(int(n) / int(p))
        return ''
    if mode == 'n':
        if p != '' and q != '':
            return str(int(p) * int(q))
        return ''
    if mode == 'phi_n':
        if p == '':
            p = rsa('p', plainText, cipherText, p, q, n, phi_n, e, d)
        if q == '':
            q = rsa('q', plainText, cipherText, p, q, n, phi_n, e, d)
        if p != '' and q != '':
            return str((int(p) - 1) * (int(q) - 1))
        return ''
    if mode == 'enc':
        if n == '':
            n = rsa('n', plainText, cipherText, p, q, n, phi_n, e, d)
        if e == '':
            e = rsa('inv', plainText, cipherText, p, q, n, phi_n, e, d)
        if plainText != '' and e != '' and n != '':
            return str(pow(int(plainText), int(e), int(n)))
        return ''
    if mode == 'dec':
        if n == '':
            n = rsa('n', plainText, cipherText, p, q, n, phi_n, e, d)
        if d == '':
            d = rsa('inv', plainText, cipherText, p, q, n, phi_n, e, d)
        if cipherText != '' and d != '' and n != '':
            return str(pow(int(cipherText), int(d), int(n)))
        return ''
    if mode == 'inv':
        if phi_n == '':
            phi_n = rsa('phi_n', plainText, cipherText, p, q, n, phi_n, e, d)
        if e != '' and phi_n != '':
            return str(inverseMod(int(e), int(phi_n)))
        if d != '' and phi_n != '':
            return str(inverseMod(int(d), int(phi_n)))
        return ''
    print('mode unrecognized')

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
    print('===' + '\n' + mode + ': ' + rsa(mode, plainText, cipherText, p, q, n, phi_n, e, d) + '\n')
