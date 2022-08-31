
#exemple3
import csv

table_exemple=[ {'nom': 'Dupont', 'prenom': 'Jean-Claude', 'age': '32'},
                {'nom': 'Duteil', 'prenom': 'Paul', 'age': '41'},
                {'nom': 'Claudon', 'prenom': 'Goery', 'age': '37'},
                {'nom': 'Tonton', 'prenom': 'Pierre', 'age': '54'},
                {'nom': 'Penard', 'prenom': 'Bob', 'age': '18'},
                {'nom': 'Herpoix', 'prenom': 'Stephane ', 'age': '55'},
                {'nom': 'Salicorne', 'prenom': 'Bruno', 'age': '15'},
                {'nom': 'Poiteau', 'prenom': 'Maxe', 'age': '33'},
                {'nom': 'Clanget', 'prenom': 'Gilles', 'age': '54'},
                {'nom': 'Luillier', 'prenom': 'Martin', 'age': '34'},
                {'nom': 'Clanget', 'prenom': 'Justine', 'age': '14'},
                {'nom': 'Gillier', 'prenom': 'Paul', 'age': '16'}]

def vers_csv(nom_de_la_table ,ordre , fichier_sortie_csv):
    # nom_de_la_table: chaine de caracteres --> table a utiliser
    # ordre: liste contenant l ordre dans lequel les valeurs doivent etre affichees
    # fichier_sortie_csv est le nom du fichier a creer

    table=eval(nom_de_la_table) # evaluation du nom de la table

    # Ouverture du fichier en ecriture
    with open( fichier_sortie_csv+'.csv',"w",newline='') as fic:
        # initialisation d un lecteur de fichier
        dic=csv.DictWriter(fic ,fieldnames=ordre)
        # Ecriture des cles sur la premiere ligne
        dic.writeheader()
        # Ecriture des differentes lignes
        for ligne in table:
            dic.writerow(ligne)
    return None

ordre = ['nom','age','prenom'] # Definition de l ordre des cles
vers_csv('table_exemple',ordre ,'sortieCSV') # Appel fonction
