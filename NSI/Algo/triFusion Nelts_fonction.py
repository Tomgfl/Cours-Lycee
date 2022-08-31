# Importation du module random
from random import randint

# declaration de la fonction fusion
def fusion(tableau,L = 1):
    # Initialisation des variables
    # indice sous tableau 1 :
    # x <-- 0
    x = 0
    
    # indice sous tableau 2 :
    # y <-- 0
    y = 0
    
    # Longueur L des sous tableaux
    # L <-- 1
    # L = 1
    
    # Tableau temporaire remplis de 0 de la taille de tableau
    Temp = [0]*len(tableau)


    # tant que L < taille (tableau)
    while L < len(tableau):
        
        # Initialisation de p
        # p <-- 0
        p = 0
        
        # tant que p+2*L < taille (tableau)
        while p+2*L <= len(tableau):
            
            #pour i allant de p à p+2*L increment 1      
            for i in range(p,p+2*L):
                
                # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein
                if x < len(tableau[p:p+L]) and y < len(tableau[p+L:p+2*L]) and tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] or y >= len(tableau[p+L:p+2*L]):

                    # Temp[i] <-- tableau[p:p+L][x]
                    Temp[i] = tableau[p:p+L][x]        

                    # incrementer x de 1
                    x += 1
                    
                # Sinon
                else:
                    # Temp[i] <-- tableau[p+L:p+2*L][y]
                    Temp[i] = tableau[p+L:p+2*L][y]
                    
                    # incrementer y de 1
                    y +=1
                    
            # Reafectation des variables
            # p <-- p+2*L
            p = p+2*L
            # x <-- 0
            x = 0
            # y <-- 0
            y = 0
        
        # tableau <-- Temp
        tableau = list(Temp)
    
        # L <-- L * 2
        L = L*2

    # retourner le tableau trier
    return tableau


# Initialisation des variables

# generation de la liste par comprehension
liste = [randint(0,200) for i in range (128)]

# Appel de la fonction fusion ( liste )
trier = fusion(liste,1)

# Affichage ecran
print(trier)








