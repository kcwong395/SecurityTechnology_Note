def inverseMod(a, m):
    for i in range(1, m):
        if (m * i + 1) % a == 0:
            return (m * i + 1) // a
    return None
