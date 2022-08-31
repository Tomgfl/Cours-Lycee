mon_dico={"Liste":"Structure de donneés permettant de regrouper des donnéés de maniere à pouvoir y accéder librement",
          "Graphe":"Un couple (V,E) avec V un ensemble de sommets et E un ensemble d'arêtes",
          "File":"Structure de données basées sur le principe : Premiers entré, premier sorti",
          "Arbre":"Structure de données constituée de sommets reliés par des arêtes",
          "Serveur":"Ordinateur dont les informations peuvent être consultées à distance par d'autres ordinateurs",
          "Table":"Tableau à deux dimensions dans le jargon des Bdd",
          "Algorithme":"Suite finie de règles et d'operations élémentaires qui permet de résoudre une classe de problèmes",
          "Balise":"Mot ou groupe de mots utilisés pour décrire un contenu",
          "Dictionnaire":"Une collection de couple('clé':valeur)"}

liste_dico=[("Liste","Structure de donneés permettant de regrouper des donnéés de maniere à pouvoir y accéder librement"),
            ("Graphe","Un couple (V,E) avec V un ensemble de sommets et E un ensemble d'arêtes"),
            ("File","Structure de données basées sur le principe : Premiers entré, premier sorti"),
            ("Arbre","Structure de données constituée de sommets reliés par des arêtes"),
            ("Serveur","Ordinateur dont les informations peuvent être consultées à distance par d'autres ordinateurs"),
            ("Table","Tableau à deux dimensions dans le jargon des Bdd"),
            ("Algorithme","Suite finie de règles et d'operations élémentaires qui permet de résoudre une classe de problèmes"),
            ("Balise","Mot ou groupe de mots utilisés pour décrire un contenu"),
            ("Dictionnaire","Une collection de couple('clé':valeur)")]

mon_dico_2 = dict(liste_dico)


print(type(mon_dico))
print(mon_dico['Graphe'])
print(mon_dico['File'])


print('Pile' in mon_dico)
mon_dico['Pile'] = "Structure de données fondée sur le pricipe : Dernier arrivé, premier sorti"

print(len(mon_dico))


cle_dico = mon_dico.keys()
for cle in cle_dico:
    print(f"{cle}  ",end='')
print()

for cle in cle_dico:
    if cle[0] == 'A':
        print(f"{cle} : {mon_dico[cle]}")

    
