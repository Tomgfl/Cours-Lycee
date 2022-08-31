
#Exo5

table1 = [ {'Nom': 'Joe','Maths' : 16,'Anglais':17,'Info':18} ,
{'Nom': 'Zoe','Maths' : 19,'Anglais':15,'Info':17} ,
{'Nom': 'Max','Maths' : 14,'Anglais':19,'Info':13}]

table2 = [ {'Nom': 'Joe','Age' : 16,'courriel ':'joe@info.fr'},
{'Nom': 'Zoe','Age' : 15,'courriel ':'zoe@info.fr'},
{'Nom': 'teo','Age' : 16,'courriel ':'teo@info.fr'},
{'Nom': 'Max','Age' : 17,'courriel ':'max@info.fr'}]

def fusion(table1,table2,cle):
    table_fusion=[]
    for ligne1 in table1:                           # Balayage des lignes de table1
        for ligne2 in table2:                       # Balayage des lignes de table2
            if ligne1[cle]==ligne2[cle]:            # Si la cle correspond
                new_ligne=ligne1                    # Recuperation de la ligne de table1
                for key in ligne2:                  # Balayage des cles de table2
                    if key!=cle:                    # A la recherche d une nouvelle cle pour la fusion
                        new_ligne[key]=ligne2[key]  # Ajout de la cle et valeur table_fusion.append(new_ligne)
                table_fusion.append(new_ligne)      # append de la nouvelle ligne
    return table_fusion

table_fusionnee = fusion(table1 ,table2 ,'Nom')
print(table_fusionnee)

