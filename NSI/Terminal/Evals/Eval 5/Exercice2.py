coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''

    # Initialisation liste_zoom
    liste_zoom = []

    # Pour chaque éléments dans liste_depart
    for elt in liste_depart :

        # Pour i allant de 0 a k(non compris)
        for i in range(k):

            # Ajout de l'élément a liste_zoom
            liste_zoom.append(elt)

    # Renvoie liste_zoom
    return liste_zoom


def zoomDessin(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''

    # Initialisation grille_zoom
    grille_zoom=[]

    # Pour chaque éléments de grille
    for elt in grille:

        # Appel de la fct zoomListe avec comme parametre elt(sous liste de grille) et k
        liste_zoom = zoomListe(elt,k)

        # Pour i allant de 0 a k(non compris)
        for i in range(k):

            # Ajout de liste_zoom a grille_zoom
            grille_zoom.append(liste_zoom)

    # Renvoie grille_zoom
    return grille_zoom
