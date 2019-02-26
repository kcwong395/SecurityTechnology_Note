# This function intends to calculate the gcd of two number


def gcd(a, b):
    if (b == 0):
        return a
    temp = a
    a = b
    b = temp % b
    return gcd(a, b)
