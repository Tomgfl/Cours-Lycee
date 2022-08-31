
#exo6
table1 = [ {'Nom': 'Joe','Maths' : 16,'Anglais':17,'Info':18} ,
{'Nom': 'Zoe','Maths' : 19,'Anglais':15,'Info':17} ,
{'Nom': 'Max','Maths' : 14,'Anglais':19,'Info':13}]

table2 = [ {'name': 'Joe','Age' : 16,'courriel ':'joe@info.fr'},
{'name': 'Zoe','Age' : 15,'courriel ':'zoe@info.fr'},
{'name': 'teo','Age' : 16,'courriel ':'teo@info.fr'},
{'name': 'Max','Age' : 17,'courriel ':'max@info.fr'}]
def fusion2(table1 ,table2,cle1,cle2=None):
    if cle2 == None:            # teste la presence de cle2
        cle2 = cle1
    table_fusion=[]
    for ligne1 in table1:                           # Balayage des lignes de table1
        for ligne2 in table2:                       # Balayage des lignes de table2
            if ligne1[cle1]==ligne2[cle2]:            # Si la cle correspond
                new_ligne=ligne1                    # Recuperation de la ligne de table1
                for key in ligne2:                  # Balayage des cles de table2
                    if key!=cle2:                    # A la recherche d une nouvelle cle pour la fusion
                        new_ligne[key]=ligne2[key]  # Ajout de la cle et valeur table_fusion.append(new_ligne)
                table_fusion.append(new_ligne)      # append de la nouvelle ligne
    return table_fusion

table_fusionnee2 = fusion2(table1 ,table2 ,'Nom','name')
print(table_fusionnee2)

