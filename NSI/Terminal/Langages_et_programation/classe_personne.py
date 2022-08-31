class Personne:
    def saisie_carac(self):
        self.Nom = input("Nom : ")
        self.Age = input("Age : ")
        self.Sexe = input("Sexe (F/M) : ")
        self.Nationalite = input("Nationalité : ")

    def affich_carac(self):
        print("Le nom de la personne est ",self.Nom,"\n"
              "Son âge : ",self.Age,"\n"
              "Son sexe : ",self.Sexe,"\n"
              "Sa nationalité : ",self.Nationalite)
        
perso = Personne()
perso.saisie_carac()
perso.affich_carac()
