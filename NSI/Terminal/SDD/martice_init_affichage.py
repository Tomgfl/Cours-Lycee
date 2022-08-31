
# initialisation matrice carre
m6 = [[0 for j in range(0,4)]for i in range(0,4)]


# pour chaque ligne
for i in m6:

    # pour chaque element de cette ligne
    for j in i:

        # affichage de tous les elements de cette ligne sous forme | 0 || 0 || 0 || 0 |
        print("| ",j," |",end='')

    # saut dde ligne 
    print()
