#exo revison 1
# ecrire u progremme qui
# affiche chaque elements de la liste
#compte le nombre delements superieurs a 39
#calcule et affiche la somme des elements paire
#d'une liste de 20 entiers choisis entre 0 et 99

#Importation du module random
import random

# 1)
# Creation liste aletoire
l = [random.randint(0,99) for i in range (20)]

n = 0
for i in l:
    if i > 39:
        n+=1
print(n)
