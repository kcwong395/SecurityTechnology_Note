# This function intends to calculate the gcd of two number


def gcd(a, b):
    if (int(b) == 0):
        return int(a)
    return gcd(int(b), int(a) % int(b))
