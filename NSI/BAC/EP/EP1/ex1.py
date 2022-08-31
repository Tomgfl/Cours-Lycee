notes = [(15,2),(9,1),(12,3)]

def moyenne(liste):
    '''liste <- [(note,coefficient),(note,coefficient),(note,coefficient)...]
    note <- float (entre 0 et 20)
    coefficient <- int (>0)
    Renvoie la moyenne pondérée'''

    total = 0
    total_coef = 0

    for i in range(len(liste)):
        total += liste[i][0] * liste[i][1]
        total_coef += liste[i][1]

    return total/total_coef
