#Programme qui calcule le PGCD entre a et b

print('Programme qui calcule le PGCD entre a et b\n')

# Affectation de a et b par l'utilisateur
a = int(input('Valeur de a : '))
b = int(input('Valeur de b : '))

#boucle por calculer le PGCD
while b != 0:
    #calcule du reste de la div euclidienne de a par b
    r = a % b
    a = b
    b = r
#affichege du PGCD
print ('Le plus grand diviseur commun est : ',a)
