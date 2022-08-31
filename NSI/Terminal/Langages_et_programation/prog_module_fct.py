# Nom : prog_module_fct.py
# role : Affichage du PGCD et du PPCM de deux entiers naturels non nuls a et b
#      : Affichage de la factorielle d'un entier naturel n
#      : Affichage de la racine carre d'un entier naturel n
# Utilisation de pgcd_ppcm_facto_module.py et de math

from math import sqrt
import sys
sys.path.append('P://NSI/langages_et_programation')
import pgcd_ppcm_facto_module


print('Calcul du PGCD(a,b), du PPCM(a,b), de n! et de racine_carre(n)n\ ')

a = int(input("Veuillez saisir l'entier a: " ))
b = int(input("Veuillez saisir l'entier b: " ))
n = int(input("Veuillez saisir l'entier n: " ))
print()

print("LE PGCD(",a,"," ,b,")est : ",pgcd_ppcm_facto_module.PGCD(a,b),"\n")
print("LE PPCM(",a,",",b, ")est : ",pgcd_ppcm_facto_module.PPCM(a,b),"\n")
print("Factorielle(",n,") = ",n,"! = ",pgcd_ppcm_facto_module.fact(n),"\n")
print("La racine carre de ",n,"est :",sqrt(n))




