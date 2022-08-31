def PGCD_recu(x,y):
    r = x % y
    if r != 0:
        return PGCD_recu(y,r)
    return (y)












def pgcd(x,y):
    if y == 0:
        return x
    else:
        pgcd(y,x%y)
