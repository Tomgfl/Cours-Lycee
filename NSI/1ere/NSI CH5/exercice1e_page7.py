
#exercice1e
import csv                     # le module pour les fichiers csv
def impor(nom):
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")
    L10=[]
    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L10.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return (L10)

def critere_depasse(CSV,champ,valeur_a_depasser):
    resultat= impor(CSV)
    #print(resultat)
    select_nom = [p for p in resultat if (int(p[champ]) > valeur_a_depasser)]
    return select_nom

extraction=critere_depasse('test','age',50)
print (extraction)
