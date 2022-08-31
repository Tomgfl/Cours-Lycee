def recherche(tab):
    resultat = []
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]-1:
            resultat.append((tab[i],tab[i+1]))
    return resultat
