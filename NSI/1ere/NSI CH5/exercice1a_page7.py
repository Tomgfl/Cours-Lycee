
#exercice1a
import csv                     # le module pour les fichiers csv
def impor(nom):
    L6=[]
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L6.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return L6

def un_critere(CSV,champ,valeur):
    resultat= impor(CSV)
    select_nom = [p for p in resultat if p[champ] == valeur]
    return select_nom

extraction=un_critere('test','nom','Clanget')
print (extraction)

