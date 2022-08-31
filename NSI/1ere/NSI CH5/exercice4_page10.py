#Exo4
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

def tri(table,attribut,decroit=False):
    table_exemple=impor(table)
    table_triee4=sorted(table_exemple, key=lambda donnees: donnees[attribut],reverse=decroit)
    return table_triee4


table_triee_crois = tri('test','age') # Tri de la table selon attribut croissant
print(table_triee_crois)
table_triee_decroi = tri('test','age',True) # Tri de la table selon attribut decroissant
print(table_triee_decroi)
