# coding: utf-8
# nom du programme : deuxPuissance_signée_algo
# rôle : calculer et afficher les puissances de l'entier 2
# propriété : l'exposant est un entier relatif


# declaration de la fonction
def deuxPuissance(exposant):

    # declaration de la fonction
    resultat = 1

    # si x(exposant) est negatif
    if exposant < 0:

        # pour i allant de 0 à la valeur absolue de l'exposant exclu
        for i in range(exposant*-1):

            # resultat = resultat / 2
            resultat /= 2
    # sinon
    else:

        # pour i allant de 0 à l'exposant exclu
        for i in range(exposant):

            # resultat = resultat * 2
            resultat *= 2
    # retourner le resultat
    return resultat





