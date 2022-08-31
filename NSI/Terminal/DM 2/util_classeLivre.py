from classeLivre import livre

# intialisation variable
#liste pour stocker les livres cree
liste_livre = []

nouveau_livre = True

while nouveau_livre:
    liste_livre.append(livre())

    ask = input("Souhaitez vous creer un nouveau livre (O/N)")
    if ask == 'N':
        nouveau_livre = False
