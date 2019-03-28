# This function intends to calculate the gcd of two number


def gcd(a, b):
    temp = a
    a = b
    b = temp % b
    if (b == 0):
        return a
    return gcd(a, b)
