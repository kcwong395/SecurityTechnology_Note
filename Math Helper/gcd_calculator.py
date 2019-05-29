# This function intends to calculate the gcd of two number


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
