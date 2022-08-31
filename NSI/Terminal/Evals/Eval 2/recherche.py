# Nom du fichier : recherche.py


# Declaration de la fonction recherche
def recherche(elt,tab):
    '''Fonction qui prend en parametre:
        elt : un nombre
        tab : un tableau de nombre
        Renvoie le tableau des indices de elt dans tab'''

    # Initialisation des variables
    # Tableau des indices de elt dans tab
    resultat = []

    # Balayage de chaque valeurs de tab
    for i in range(len(tab)):
        
        # Si elt = tab[i]
        if elt == tab[i]:

            # Ajout de l'indice dans le tableau resultat
            resultat.append(i)
            
    # Renvoie le resultat
    return resultat
            
