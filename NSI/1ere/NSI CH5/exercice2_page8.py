
#exo2

import csv

def impor(nom):
    file = open(nom+'.csv',"r")   # ouvrir le fichier nom.csv en lecture

# initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    list_dico = []
    for ligne in csv_en_dico : # parcours du lecteur avec une boucle
        list_dico.append(dict(ligne))
    file.close () # fermeture du fichier
    return(list_dico)

table_exemple=impor('test')
liste_attributs = ['prenom','age']

def projection (table:list,liste_attributs=list):
    # Lignes a completer
    resultat= [{cle:ligne[cle] for cle in ligne if cle in liste_attributs} for ligne in table]
    return resultat

resultat = projection(table_exemple , liste_attributs)
print(resultat)

