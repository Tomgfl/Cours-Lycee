# Module de fonctions regroupant:
# -la fonction pgcd
# -la fonction ppcm
# -la fonction factorielle


def PGCD(x,y):
    ''' Programme qui calcule le plus grand diviseur commun entre 2 entiers naturels '''
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def PPCM(x,y):
    ''' Programme qui calcule le plus petit commun multiple entre 2 entiers naturels '''
    a,b = x,y
    while y != 0:
        r = x % y
        x = y
        y = r
    return (int((a*b)/x))


def fact(x):
    ''' Programme qui calcule la factorielle d'un entiers naturels '''
    f = 1
    for i in range(1,x+1):
        f *= i
    return f







