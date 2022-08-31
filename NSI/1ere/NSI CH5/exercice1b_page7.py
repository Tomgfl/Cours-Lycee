#exercice1b
import csv                     # le module pour les fichiers csv
def impor(nom):
    L7=[]
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L7.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return L7

def criteres_ou(CSV,champ1,valeur1,champ2,valeur2):
    resultat= impor(CSV)
    select_nom = [p for p in resultat if p[champ1] == valeur1 or p[champ2] == valeur2]
    return select_nom

extraction=criteres_ou('test','nom','Clanget','prenom','Paul')
print (extraction)