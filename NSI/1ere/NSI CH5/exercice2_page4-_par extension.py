#exercice2 liste de liste extension
import csv                    # le module pour les fichiers csv
def csv_list_de_list_ext(nom):
    file = open(nom , "r")   # ouvrir le fichier
    # initialisation d un lecteur de fichier delimiter est facultatif
    csv_en_liste = csv.reader(file , delimiter = ",")
    L2b=[]
    for ligne in csv_en_liste :     # parcours du lecteur avec une boucle
        L2b.append(ligne)
    file.close ()
    return L2b
nom='test.csv'
maListeDeListe=csv_list_de_list_ext(nom)
print(maListeDeListe)
