
# Arbre
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(arbre,lettre):
    '''Fonction taille qui prend en parametre
    - arbre : un arbre binaire de caractères
    - lettre : la valeur du sommet de l'arbre
    Et qui renvoie le nombre total de noeud de l'arbre
    '''

    #fils gauche = arbre[lettre][0]
    #fils droit = arbre[lettre][1]


    # Aucun des 2 fils n'est ''
    if arbre[lettre][0] != '' and arbre[lettre][1] != '':

        # Appel recursif de 1 + taille du fils droit et gauche
        return 1 + taille(arbre,arbre[lettre][0]) + taille(arbre,arbre[lettre][1])


    # Sinon si seulement le fils gauche n'est pas ''
    elif arbre[lettre][0] != '':

        # Appel recursif 1 + taille arbre gauche
        return 1 + taille(arbre,arbre[lettre][0])


    # Sinon si seulement le fils droit n'est pas ''
    elif arbre[lettre][1] != '':

        # Appel recursif 1 + taille arbre droit
        return 1 + taille(arbre,arbre[lettre][1])


    # Sinon les 2 fils sont ''
    else:

        # Renvoie 0
        return 0


