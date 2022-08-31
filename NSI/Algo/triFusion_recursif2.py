# declaration de la fonction recursif (liste, taille_segment, position_du_premiers_element)
def recursif(tableau,L,p):
    
    # Cas de base
    
    # Si L >= taille(tableau)
    if L >= len(tableau):
        
        # retourner le tableau
        return tableau


    # Si p+2*L > taille(tableau)
    if p+2*L > len(tableau):

        # Appel recursif(tableau, 2*taille_segment, 0)
        return recursif(tableau,2*L,0)

    
    # Initialisation des variables
    # indice sous tableau 1 :
    # x <-- 0
    x = 0
    
    # indice sous tableau 2 :
    # y <-- 0
    y = 0
    
    
    # Tableau temporaire vide
    Temp = []
  

    # Pour i allant de p a p+2*L
    for i in range(p,p+2*L):
            
        # Si tableau[p:p+L] ET tableau[p+L:p+2*L] non pleins ET tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] OU tableau[p+L:p+2*L] plein
        if x < len(tableau[p:p+L]) and y < len(tableau[p+L:p+2*L]) and tableau[p:p+L][x] <= tableau[p+L:p+2*L][y] or y >= len(tableau[p+L:p+2*L]):

            # Add Temp <-- tableau[p:p+L][x]
            Temp.append(tableau[p:p+L][x])

            # x <-- x+1
            x +=1
            
        # Sinon
        else:
                
            # Add a Temp <-- tableau[p+L:p+2*L][y]
            Temp.append(tableau[p+L:p+2*L][y])

            # y <-- y+1
            y += 1

    
    # I <-- tableau[0:p] + Temp + tableau[p+len(Temp):]
    # Appel recursif (I,L,p+2*L)
    return recursif(tableau[0:p] + Temp + tableau[p+len(Temp):],L,p+2*L)






# Importation du module random
from random import randint

# generation de la liste par comprehension
liste = [randint(0,200) for i in range (128)]

# Appel de la fonction recursif (liste,1)
trier = recursif(list(liste),1,0)

# Affichage ecran
print(trier)
