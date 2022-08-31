# declaration de la fonction recursif (liste, tailleSegment)
    
    # Cas de base
    # Si L >= taille(tableau)
    
        # retourner le tableau
    
    # Initialisation des variables
    # indice sous tableau 1 :
    # x <-- 0
    
    # indice sous tableau 2 :
    # y <-- 0

    # Tableau temporaire remplis de 0 de la taille de tableau

    # initialisation de p
    # p <-- 0

    # Tant que p+2*L <= taille(tableau)

        # Pour i allant de p a p+2*L
            
            # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein

                # Temp[i] <-- tableau[p:p+L][x]

                # x <-- x+1
                
            # Sinon
                
                # Temp[i] <-- tableau[p+L:p+2*L][y]

                # y <-- y+1
                
        # Reafectation des variables
        # p <-- p+2*L
        # x <-- 0
        # y <-- 0    

    # retourner recursif(Temp,2*L)



# Importation du module random

# generation de la liste par comprehension

# Appel de la fonction recursif (liste,1)

# Affichage ecran
