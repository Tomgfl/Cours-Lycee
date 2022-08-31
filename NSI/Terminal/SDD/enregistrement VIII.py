
# Declaration de la fonction pour l'enregistrement
def enregistrement(sdd):

    # Recuperation clavier des données de l'article
    code = int(input("Veuillez entrer un code article : "))
    nom = input("Veuillez entrer la dénomination de l'article : ")
    prix = float(input("Veuillez entrer le prix de l'article : "))
    stock = int(input("Veuillez entrer le stock de l'article : "))
    print()

    # Ajout des données a la sdd
    sdd.append({'Code':code,'Dénomination':nom,'Prix':prix,'Stock':stock})



# Main

# initialisation des variables
sdd_stock = []

# Entree clavier du nombre d'enregistrement
nb_enregistrement = int(input("Nombre d'enregistrement : "))

# Boucle d'enregistrement
for i in range(nb_enregistrement):
    enregistrement(sdd_stock)

# Affichage ecran
print(sdd_stock)
