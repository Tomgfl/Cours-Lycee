
#Exercice4
import csv

# creation d’une liste de dictionnaire a partir d »un fichier csv (exo3)
def impor(nom):
    file = open(nom+'.csv' , "r")   # ouvrir le fichier nom.csv en lecture

    # initialisation d un lecteur de fichier avec creation automatique de dictionnaire
    csv_en_dico = csv.DictReader(file , delimiter = ",")

    list_dico = []
    for ligne in csv_en_dico :      # parcours du lecteur avec une boucle
        list_dico.append(dict(ligne))
    file.close ()                   # fermeture du fichier
    return(list_dico)

def ajout(fichier):
    # creation d’une liste de dictionnaire avec l’appel de la fonction import
    fichier_importe = impor(fichier)
    # saisie par l’utilisateur du Nom, Prenom, et des notes NSI, Physique, Math dans trois fenêtres successives
        #(exemple : lieu=input(‘saisir le lieu’)
    nom = input("Nom:")
    prenom = input("Prenom:")
    nsi = input("NSI:")
    physique = input("Physique:")
    maths = input("Maths:")

    # Ajout des entrees utilisateur dans la liste de dictionnaire
    fichier_importe.append({"Nom":nom , "Prenom":prenom , "NSI":nsi , "Physique":physique , "Maths":maths})

    # Definition de l ordre
    ordre = ["Nom","Prenom","NSI","Physique","Maths"]

    # Ecriture dans le fichier csv
    with open(fichier+'.csv' , 'w',newline='') as fic:             # Ouverture du fichier a ecrire
        dic = csv.DictWriter(fic,fieldnames = ordre)               # initialisation d’un lecteur de fichier
        dic.writeheader()                                          # Ecriture des cles sur la premiere ligne
        for ligne in fichier_importe:                              # Ecriture des differentes lignes
            dic.writerow(ligne)

    return None

ajout("fichier")

