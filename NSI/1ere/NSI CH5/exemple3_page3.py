#exemple3

import csv                      # le module pour les fichiers csv
file = open("test.csv" , "r")   # ouvrir le fichier

# initialisation d un lecteur de fichier avec creation automatique de dictionnaire
csv_en_dico = csv.DictReader(file , delimiter = ",")

for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
    print(dict(ligne))          # affichage ligne a ligne

file.close ()                   # fermeture du fichier
