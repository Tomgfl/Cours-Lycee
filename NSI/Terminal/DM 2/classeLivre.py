

class livre:

    def __init__(self):
        print("*** Bienvenue dqns le programme de création d'un livre ***")
        self.constructeur()
        print()
        self.affichage()

    def constructeur(self):
        self.saisie_titre()
        self.saisie_auteur()
        self.saisie_editeur()
        self.saisie_page()
        self.saisie_annee()

    def saisie_titre(self):
        self.titre = input("Titre : ")

    def saisie_auteur(self):
        self.auteur = input("Auteur : ")

    def saisie_editeur(self):
        self.editeur = input("Editeur : ")

    def saisie_page(self):
        self.pages = int(input("Nombre de pages : "))

    def saisie_annee(self):
        self.annee = int(input("Annee de parution : "))

    def affichage(self):
        print("Vous avez cree un livre qui possede les proprietés suivantes :")
        print(f"Titre : {self.titre}\n"
              f"Auteur : {self.auteur}\n"
              f"Editeur : {self.editeur}\n"
              f"Nombre de Pages {self.pages}\n"
              f"Année de parution : {self.annee}")

        
 




