# coding: utf-8
# nom du programme : nPuissance_signée_fonction_récursive_algo
# rôle : calculer et afficher les puissances de l'entier n
# propriété : appelle la récursive fonction nPuissance
#           : l'entier et l'exposant sont des entiers relatifs
#           : le programme vérifie le type des entrées clavier et
#           : rejette toute entrée clavier non conforme 


# declaration de la fonction
def nPuissance(x,y):

    # verification try
    try:
        # verification que x est un entier relatif
        assert type(x) == int
        # verification que y est un entier relatif
        assert type(y) == int
    # except une erreur
    except:

        #affichage du message d'erreur
        print("Erreur de saisie : l'entier et l'exposant sont des entiers relatifs")
    

    # si l'exposant est nul
    if y == 0:
        # retourner 1
        return 1
    # sinon si l'exposant est negatif
    elif y < 0:
        #retourner 1 / par x la fonction de parametre x et la valeur absolue de y
        return 1/nPuissance(x,y*-1)
    # sinon 
    else :
        # retourner x*la fonction recursive de parametre x et y-1 
        return x*nPuissance(x,y-1)


#debut du programme

# affichage de l'énoncer du programe
print("Calcul de x puissance y ,x et y entiers relatifs\n")

# verification des valeurs
try:
    # verification de l'entier x
    a = int(input("Entrez la valeur de l'entier x : "))
    # verification de l'exposant entier y 
    b = int(input("Entrez la valeur de l'exposant y : "))
# except erreur
except:
    # message erreur
    print("Erreur de saisie : l'entier et l'exposant sont des entiers relatifs\n")

# affichage resultat
print(f"{a} puissance {b} = {nPuissance(a,b)}")




    
