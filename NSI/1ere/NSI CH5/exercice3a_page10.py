
#Exo3a
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
table_triee=sorted(table_exemple, key=lambda donnees: donnees["age"])

# Ecriture dans le fichier table_age_croi.csv
with open('table_age_croi.csv' , 'w',newline='') as fic:             # Ouverture du fichier a ecrire
    ordre = ['nom','prenom','age']                             # définition ordre des colonnes
    dic = csv.DictWriter(fic,fieldnames = ordre)               # initialisation d’un lecteur de fichier
    dic.writeheader()                                          # Ecriture des cles sur la premiere ligne
    for ligne in table_triee:                              # Ecriture des differentes lignes
        dic.writerow(ligne)


