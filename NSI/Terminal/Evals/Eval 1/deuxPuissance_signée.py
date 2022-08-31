# coding: utf-8
# nom du programme : deuxPuissance_signée_algo
# rôle : calculer et afficher les puissances de l'entier 2
# propriété : l'exposant est un entier relatif

# Initilisation des variables et constantes
# exposant <-- 0
exposant = 0

# résultat <-- 1
resultat = 1


# Entrée clavier de l'exposant
exposant = int(input("Veuillez saisir l'exposant : "))


# Traitement du signe de l'exposant
# Si l'exposant est négatif
if exposant < 0:

    #Pour i allant de 0 à la valeur absolue de l'exposant exclu
    
    for i in range(exposant * -1):
        # resultat <-- resultat / 2
        resultat /= 2

# Sinon
else:
    # Pour i allant de 0 à l'exposant exclu
    for i in range(exposant):

        # resultat <-- resultat *2
        resultat *= 2

# Afficher le résultat (sortie écran)
print(f"Le resultat de 2 puissance {exposant} est {resultat}")


