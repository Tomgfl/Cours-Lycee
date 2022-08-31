# # nom du programme : suite_while_l_algo.py
# rôle : calculer et afficher les termes d'une suite arithmétique dont la relation  de récurrence est U0 = 100
#                                                                                                     Un+1 = 3*Un + 4

# Initialisation des variables et constantes
U = 100
n = 0
i = True

# Entrée clavier du rang de calcul
rang = int(input())

# Tant que le rang de calcul saisi n'est pas atteint
while i :

    # Afficher le terme d'indice n
    print(U)
 
    # Calculer le terme d'indice n+1
    U = 3*U+4

    # Si le rang de calcul saisi est atteint
    if rang == n+1 :

        # Rendre vraie la condition de fin de boucle
        i = False

    # incrémenter l'indice n
    n+=1


a = input()
