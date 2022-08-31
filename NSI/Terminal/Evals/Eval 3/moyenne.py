# nom_du_programme : moyenne.py
# rôle : La fonction moyenne renvoie la moyenne d'un tableau non vide de nombre flottants


# Declaration de la fonction moyenne
def moyenne(tableau):
    """ Fonction qui renvoie la moyenne d'un tableau non vide de nombre flottants
        - type(tableau) = list"""
    
    # Verification que le parametre tableau est une liste
    assert type(tableau) == list,"Erreur : tableau doit etre une liste"
    
    # Verification que le tableau est remplis
    assert len(tableau) > 0 ,"Erreur : le tableau ne doit pas etre vide"
    
    # Initialisation de la variable total_valeurs
    # total_valeurs <- 0
    total_valeurs = 0

    # Pour chaque valeurs du tableau
    for valeur in tableau:

        # Verification que la valeur est valide
        assert type(valeur) == float, "Erreur : la valeur dans le tableau n'est pas un nombre flotant"

        # Ajout de la valeur au total_valeurs
        # total_valeurs <- total_valeurs + valeur
        total_valeurs += valeur

    # Renvoie du resultat (moyenne = total_valeurs/nombre d'element du tableau
    return total_valeurs/len(tableau)




#correcteur : J. BEAU
# note: 5/5

