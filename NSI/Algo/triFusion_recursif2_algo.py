# declaration de la fonction recursif (liste, taille_segment, position_du_premiers_element)
    
    # Cas de base
    
    # Si L >= taille(tableau)
        
        # retourner le tableau

    # Si p+2*L > taille(tableau)

        # Appel recursif(tableau, 2*taille_segment, 0)

    
    # Initialisation des variables
    # indice sous tableau 1 :
    # x <-- 0
    
    # indice sous tableau 2 :
    # y <-- 0
    
    
    # Tableau temporaire vide
  

    # Pour i allant de p a p+2*L
            
        # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein

            # Add Temp <-- tableau[p:p+L][x]

            # x <-- x+1
            
        # Sinon
                
            # Add Temp <-- tableau[p+L:p+2*L][y]

            # y <-- y+1


    # I <-- tableau[0:p] + Temp + tableau[p+len(Temp):]
    # Appel recursif (I,L,p+2*L)






# Importation du module random

# generation de la liste par comprehension

# Appel de la fonction recursif (liste,1)

# Affichage ecran
