
# initialisation matrice carre
m6 = [[0 for j in range(0,40)]for i in range(0,40)]


### AFFICHAGE ###

# Affichage de letters des lignes

# affichage de l'espace
print("  ",end="")

for i in range(len(m6)):
    
    # affichage de chaque lettre apres le A(chr65)
    print(f"| {chr(65+i)} |",end='')

# chagement de ligne
print()


# pour chaque ligne
for i in range(len(m6)):

    # affichage des lettres de colone
    print(f"{chr(65+i)} ",end='')
    # pour chaque element de cette ligne
    for j in m6[i]:

        # affichage de tous les elements de cette ligne sous forme | 0 || 0 || 0 || 0 |
        
        print(f"| {j} |",end='')

    # changement de ligne 
    print()
