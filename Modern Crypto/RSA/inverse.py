def inverseMod(a, m):
    for i in range(1, int(m)):
        if (int(m) * i + 1) % int(a) == 0:
            return (int(m) * i + 1) // int(a)
    return None
