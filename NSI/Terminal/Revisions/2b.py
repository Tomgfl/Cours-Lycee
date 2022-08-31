#exo revison 1
# ecrire u progremme qui
# affiche chaque elements de la liste
#compte le nombre delements superieurs a 39
#calcule et affiche la somme des elements paire
#d'une liste de 20 entiers choisis entre 0 et 99

#Importation du module random

from random import randint

# Creation liste aletoire
l_alea = [randint(0,99) for i in range (20)]

#initialisation de la 2e liste et des variables
l_sup_a_39 = []
somme = 0

#recherche des valeurs superieurs a 39 et les additionne 
for i in l_alea:
    if i > 39:
        somme += i
        l_sup_a_39.append(i)

#tri de la liste decroissante
l_sup_a_39.sort(reverse = True)

#affichage
print("il y a ",len(l_sup_a_39),"valeurs superieur a 39")
print("la somme des valeurs est ",somme)
print("les valeurs par ordre decroissant: ",l_sup_a_39)


