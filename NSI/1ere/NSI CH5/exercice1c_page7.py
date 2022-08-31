#exercice1c
import csv                     # le module pour les fichiers csv
def impor(nom):
    L8=[]
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L8.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return L8

def criteres_et_non(CSV,champ1,valeur1,champ2,valeur2):
    resultat= impor(CSV)
    select_nom = [p for p in resultat if p[champ1] == valeur1 and not p[champ2] == valeur2]
    return select_nom

extraction=criteres_et_non('test','nom','Clanget','prenom','Justine')
print (extraction)

