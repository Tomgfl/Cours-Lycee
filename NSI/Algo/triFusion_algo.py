# initialisation de variables

# indice sous tableau 1 :
# x <-- 0

# indice sous tableau 2 :
# y <-- 0

# tableau <-- [9,46,26,72,15,46,33,8]

# Longueur L des sous tableaux
# L <-- 1

# Tableau temporaire remplis de 0 de la taille de tableau
# Temp <-- []

# p <-- 0


# tant que L < taille (tableau)

    # Initialisation de p
    # p <-- 0
    
    # tant que p+2*L < taille (tableau)

        #pour i allant de p à p+2*L increment 1
                  

            # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein
            
                #Temp[i] <-- tableau[p:p+L][x]

                # incrementer x de 1

            # Sinon

                # Temp[i] <-- tableau[p+L:p+2*L][y]
                
                # incrementer y de 1

        # Reafectation des variables
        # p <-- p+2*L
        # x <-- 0
        # y <-- 0

    # tableau <-- Temp
    
    # L <-- L * 2



# Affichage ecran tableau

    
    
