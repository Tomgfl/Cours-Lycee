

def correspond(mot,mot_a_trou):
    '''Prend en paramètre un mot et un mot a trou contenant uniquement des
    majuscules et des *
    Renvoie True si on peut obtenir mot en remplaçant convenablement les
    caractères * de mot a trou et False sinon'''

    if len(mot) != len(mot_a_trou):
        return False

    for c in range(len(mot_a_trou)):
        if not(mot_a_trou[c] == mot[c] or mot_a_trou[c] == "*"):
            return False
    return True



