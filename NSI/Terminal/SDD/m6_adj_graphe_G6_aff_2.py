
# initialisation matrice carre
m6 = [[0 for j in range(0,4)]for i in range(0,4)]

m6 = [[0,1,0,1],[1,0,1,1],[0,1,0,0],[1,1,0,0]]



### AFFICHAGE ###

# Affichage de letters des lignes

# affichage de l'espace
print("  ",end="")

for i in range(len(m6)):
    
    # affichage de chaque lettre apres le A(chr65)
    print(f"|     {chr(65+i)}     |",end='')

# chagement de ligne
print()


# pour chaque ligne
for i in range(len(m6)):

    # affichage des lettres de colone
    print(f"{chr(65+i)} ",end='')
    # pour chaque element de cette ligne
    for j in range(len(m6[i])):

        # affichage de tous les elements de cette ligne sous forme | 0 || 0 || 0 || 0 |
        
        print(f"| m6({i+1},{j+1})={m6[i][j]} |",end='')

    # changement de ligne 
    print()
