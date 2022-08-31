def PGCD(x,y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x