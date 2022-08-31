
#exercice2 liste de liste compréhension
import csv                    # le module pour les fichiers csv
def csv_list_de_list_comp(nom):
    file = open(nom , "r")   # ouvrir le fichier
    # initialisation d un lecteur de fichier delimiter est facultatif
    csv_en_liste = csv.reader(file , delimiter = ",")
    L2t=[ligne for ligne in csv_en_liste]

    #file.close ()
    return L2t
nom='test.csv'
maListeDeListe=csv_list_de_list_comp(nom)
print(maListeDeListe)