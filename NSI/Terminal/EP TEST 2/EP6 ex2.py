

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire plan correspondant à un plan d'envoie
    de messages entre N personnes A, B, C, D, E, F ... (avec N <= 26)
    Renvoie True si le plan d'envoie de messages est cyclique et False sinon'''

    personne = 'A'
    N = len(plan)
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True

