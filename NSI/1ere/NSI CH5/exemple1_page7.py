#Exemple1 page7
import csv                     # le module pour les fichiers csv
def impor(nom):
    L5=[]
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L5.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return L5

resultat= impor('test')
select_nom = [p for p in resultat if p['nom'] == 'Clanget']
print (select_nom)

