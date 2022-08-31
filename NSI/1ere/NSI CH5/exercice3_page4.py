
#exercice3 liste de dictionnaires
import csv                     # le module pour les fichiers csv
def impor(nom):
    L4b=[]
    file = open(nom+".csv" , "r")   # ouvrir le fichier

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        L4b.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return L4b
nom='test'
maListeDeDict=impor(nom)
print(maListeDeDict)

