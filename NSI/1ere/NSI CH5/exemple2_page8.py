
#exemple 2

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

# ##################################################################
resultat=impor('test')
# Selection des colonnes qui ont pour cle 'nom' ou 'age'
select_colonne= [{cle:ligne[cle] for cle in ligne if cle in ['nom','age']} for ligne in resultat]
print (select_colonne)


