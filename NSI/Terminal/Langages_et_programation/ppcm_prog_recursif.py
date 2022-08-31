import pgcd_prog_recursif

def PPCM_recu(x,y):
    return int(x*y/pgcd_prog_recursif.PGCD_recu(x,y))
