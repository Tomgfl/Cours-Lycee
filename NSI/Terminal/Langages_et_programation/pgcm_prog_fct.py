def PPCM(x,y):
    a,b = x,y
    while b != 0:
        r = x % y
        x = y
        y = r
    return (int((a*b)/x))
