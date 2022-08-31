# declaration de la fonction recursif (liste, tailleSegment)
def recursif(tableau,L):
    
    # Cas de base
    # Si L >= taille(tableau)
    if L >= len(tableau):
        # retourner le tableau
        return tableau
    
    # Initialisation des variables
    # indice sous tableau 1 :
    # x <-- 0
    x = 0
    
    # indice sous tableau 2 :
    # y <-- 0
    y = 0

    # Tableau temporaire remplis de 0 de la taille de tableau
    Temp = [0]*len(tableau)

    # initialisation de p
    # p <-- 0
    p = 0

    # Tant que p+2*L <= taille(tableau)
    while p+2*L <= len(tableau):

        # Pour i allant de p a p+2*L
        for i in range(p,p+2*L):
            
            # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein
            if x < len(tableau[p:p+L]) and y < len(tableau[p+L:p+2*L]) and tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] or y >= len(tableau[p+L:p+2*L]):

                # Temp[i] <-- tableau[p:p+L][x]
                Temp[i] = tableau[p:p+L][x]

                # x <-- x+1
                x +=1
            # Sinon
            else:
                
                # Temp[i] <-- tableau[p+L:p+2*L][y]
                Temp[i] = tableau[p+L:p+2*L][y]

                # y <-- y+1
                y += 1
        # Reafectation des variables
        # p <-- p+2*L
        p = p+2*L
        # x <-- 0
        x = 0
        # y <-- 0    
        y = 0

    # retourner recursif(Temp,2*L)
    return recursif(Temp,2*L)



# Importation du module random
from random import randint

# generation de la liste par comprehension
liste = [randint(0,200) for i in range (128)]

# Appel de la fonction recursif (liste,1)
trier = recursif(liste,1)

# Affichage ecran
print(trier)
