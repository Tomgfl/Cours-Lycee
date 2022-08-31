# Importation des modules nécessaires
from tkinter import *
from tkinter.ttk import *

prixmin = None




# Initialisation de la fenetre
master = Tk()

# Création de la zone de texte 1
label1= Label(master, text="Entrez votre recherche :")
# Ancrage de la zone de texte 1
label1.grid(row=0, column=0,padx=5,pady=5)

# Création de la barre de recherche
recherche = Entry(master)
# Ancrage de la barre de recherche
recherche.grid(row = 1, column = 0, sticky = W, pady = 2,padx=5) 

# Définition de la fonction recupere() qui récupère les valeurs de toutes les entrées et les attribue aux variables liées
def recupere():
    global prixmin
    motrecherche = recherche.get()
    prixmin = pmin.get()
    prixmax= pmax.get()
    nombrearticle= nbart.get()
    vinted = vint.get()
    facebook= face.get()
    topannonces= topa.get()
    print(prixmin)

# Création du bouton valider qui déclenche la fonction recupere
bouton = Button(master, text="Valider", command=recupere)
# Ancrage du bouton
bouton.grid(row = 2,column = 0, sticky = W, pady= 2, padx=27)

# Création de la zone de texte 2
label2 = Label(master, text= "Prix minimum :")
# Ancrage de la zone de texte 2
label2.grid(row = 0, column = 1,sticky = E, pady=5)

# Création de l'entrée du prix minimal
pmin = Entry(master,width=7)
# Ancrage de celle ci
pmin.grid(row = 0, column= 2, pady= 5)

# Création de la zone de texte 3
label3 = Label(master, text= "Prix maximum :")
# Ancrage de la zone de texte 3
label3.grid(row = 1, column = 1,sticky = E, pady=5)

# Création de l'entrée du prix minimal
pmax = Entry(master,width=7)
# Ancrage de celle-ci
pmax.grid(row = 1, column= 2, pady= 5)

# Création de la zone de texte 4
label4 = Label(master, text= "Nombre d'articles par site :")
# Ancrage de la zone de texte 4
label4.grid(row = 2, column = 1, pady=5)

# Création de l'entrée du nombre d'articles par site
nbart = Entry(master,width=7)
# Ancrage de celle-ci
nbart.grid(row = 2, column= 2, pady= 5)

# Initialisation de la variable entière vint
vint= IntVar()
# Création de la case à cocher qui correspond à la variable vint
vt = Checkbutton(master, text="Vinted",variable = vint)
# Ancrage de celle-ci
vt.grid(row = 0, column = 3, pady = 5,padx = 10, sticky = W)

# Initialisation de la variable entière face
face = IntVar()
# Création de la case à cocher qui correspond à la variable face
fb = Checkbutton(master, text="Facebook Marketplace",variable = face)
# Ancrage de celle-ci
fb.grid(row = 1, column = 3,padx = 10, pady = 5, sticky = W)

# Initialisation de la variable entière topa
topa = IntVar()
# Création de la case à cocher qui correspond à la variable topa
ta = Checkbutton(master, text="Top Annonces",variable = topa)
# Ancrage de celle-ci
ta.grid(row = 2, column = 3, pady = 5,padx = 10, sticky = W)



