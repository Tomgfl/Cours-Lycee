#Calcule de la factorielle d'un entier naturel n

#initialisation
#n <- 0
#i <- 0
#factorielle <- 1
n,i,factorielle = 0,0,1

#presentation du programme
print("Calcule de la factorielle d'un entier naturel n \n")

#lire n
n = int(input('Valeur de n : '))

if n != 0:
    #boucle de calcule factorielle
    #pour
    for i in range(1,n+1):
        #factorielle <- factorielle*i
        factorielle = factorielle*i
    #fin pour

print(factorielle)
print()
