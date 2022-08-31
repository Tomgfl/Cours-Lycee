l = [10,20,30,40,60,110]

def moyenne(liste):
    '''Fonction moyenne
    - Prend en paramètre : une liste d'entiers
    - Renvoie la moyenne des valeurs de cette liste
    '''

    # Initialisation du total
    total = 0

    # Pour chaque éléments de la liste
    for i in liste:

        # Ajoute au total cet élément
        total += i

    # Renvoie la moyenne  (total/nb d'éléments)
    return total/len(liste)

