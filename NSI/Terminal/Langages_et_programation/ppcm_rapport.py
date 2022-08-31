#Programme qui calcule le PPCM entre 2 entiers naturels

#initialisation des variables
a,b,c,d = 0,0,0,0

#presentation du programme
print('Programme qui calcule le PPCM entre 2 entiers naturels')

#saut de ligne
print ()

#lire a et b
a = int(input('Valeur de a : '))
b = int(input('Valeur de b : '))

#copie de a et b dans b et c
c,d = a,b

#calcule PGCD
while b != 0:
    r = a % b
    a = b
    b = r

#saut de ligne
print()

#affichage resultat
print(int((c*d)/a))
print()
