# coding: utf-8
# nom du programme : deuxPuissance_algo.py
# rôle : calculer et afficher les puissances de l'entier 2

# Initilisation des variables et constantes
# exposant <-- 0
exposant = 0

# résultat <-- 1
resultat = 1



# Entrée clavier de l'exposant
exposant = int(input("Veuillez saisir l'exposant : "))


# Pour i allant de 0 à l'exposant exclu
for i in range(0,exposant):


    # résultat <-- resultat * 2
    resultat *= 2


# Afficher le résultat (sortie écran)
print(f"Le resultat de 2 puissance {exposant} est {resultat}")




