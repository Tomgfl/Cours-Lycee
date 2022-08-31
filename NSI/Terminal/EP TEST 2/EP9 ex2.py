

def trouver_intrus(tab,g,d):
    if g == d:
        return tab[g]

    else:
        nombre_de_triplet = (d - g)//3
        indice = g+3*(nombre_de_triplet//2)

        if tab[indice] == tab[indice+1]:
            return trouver_intrus(tab,indice+3,d)
        else:
            return trouver_intrus(tab,g,indice)