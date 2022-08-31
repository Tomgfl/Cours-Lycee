# nom du programme : dec_to_bin.py
# rôle : La fonction dec_to_bin revoie l'ecriture binaire d'un entier positif


# Declaration de la fonction dec_to_bin
def dec_to_bin(a):
    """ Fonction qui renvoie l'ecriture binaire d'un entier positif
        - type(a) = int"""

    # Verification que a est positif 
    assert a >= 0, "Erreur : a est negatif"

    # Verification que a est un entier
    assert type(a) == int, "Erreur : a doit etre un entier"
    
    # Initialisation de bin_a
    # bin_a <- reste de la division euclidienne de a par 2
    # bin_a est une chaine de caractere
    bin_a = str(a%2)

    # a <- quotient de la division euclidienne de a par 2
    a = a//2

    # Tant que a est different de 0
    while a != 0:

        # Ajout a la chaine de caractere bin_a le reste de la division euclidienne de a par 2
        bin_a = str(a%2) + bin_a

        # a <- quotient de la division euclidienne de a par 2
        a = a//2

    # Renvoie le resultat
    return bin_a

#correcteur : J. BEAU
# note: 5/5

