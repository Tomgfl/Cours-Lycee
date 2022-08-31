#exemple1

dic={'Nom':'Baron','Prénom':'Paul','NSI':'18','Physique ':'16','Maths':'15'}

ma_table= \
    [{'Nom':'Baron','Prénom':'Paul','NSI':'18','Physique ':'16','Maths':'15'},
     {'Nom':'Taillant','Prénom':'Greg','NSI':'1','Physique':'3','Maths':'5'},
     {'Nom':'Gourdy','Prénom':'Zoé','NSI':'14','Physique ':'13','Maths':'16'}]

#exemple2
import csv                     # le module pour les fichiers csv
file = open("test.csv" , "r")   # ouvrir le fichier

# initialisation d un lecteur de fichier delimiter est facultatif
csv_en_liste = csv.reader(file , delimiter = ",")

for ligne in csv_en_liste :     # parcours du lecteur avec une boucle
    print(ligne)                    # affichage ligne a ligne
file.close ()                   # fermeture du fichier