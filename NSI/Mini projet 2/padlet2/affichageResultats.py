# Importation des modules nécessaires
from tkinter import *
from tkinter.ttk import *
from classeArticle import Article
import urllib.request
import cv2
import numpy as np
import webbrowser

# Initialisation de la variable ID
ID = 0

# Définition de la fonction hyperlien(url) qui ouvre un navigateur et accède à l'url rentrée en paramètre
def hyperlien(url):
   webbrowser.open_new_tab(url)

# Définition de la fonction fsuivant() qui permet de passer à l'annonce suivante
def fsuivant(tri):
    # Récupération des variables globales
    global ID
    global aff
    # Incrémentation de l'ID
    ID += 1
    # Fermeture de la fenêtre master
    aff.destroy()
    # Appel de la fonction affiche()
    affiche(tri)

# Définition de la fonction fprecedent() qui permet de passer à l'annonce precedente
def fprecedent(tri):
    # Récupération des variables globales
    global ID
    global aff
    # Incrémentation de l'ID (négative car on recule)
    ID += -1
    # Fermeture de la fenêtre master
    aff.destroy()
    # Appel de la fonction affiche()
    affiche(tri)

# Définition de la fonction affiche qui permet l'affichage d'une seule annonce
def affiche(tri):
    # Récupération des variables globales
    global ID
    global aff
    # L'article art à afficher est l'élément de tri d'id ID
    art = tri[ID]
    # Initialisation de la fenêtre
    aff = Tk()

    # Téléchargement de l'image de l'annonce
    urllib.request.urlretrieve(art.url_img,"image.png")
    # Chargement de cette image dans la variable img de classe cv2.imread
    img = cv2.imread("image.png")
    # Chargement de l'image redimensionnée dans la variable res
    res = cv2.resize(img, dsize=(200,300), interpolation=cv2.INTER_CUBIC)
    # Enregistrement de l'image redimensionnée
    cv2.imwrite("image.png", res)

    # Chargement de l'image redimensionnée dans la variable img de classe PhotoImage
    img = PhotoImage(file = "image.png")
    # Ajout de cette image à la fenetre master et ancrage de celle ci
    Label(aff, image = img).grid(row = 0, column = 0,columnspan = 2, rowspan = 1, padx = 5, pady = 5)
    # Ajout du nom à la fenetre master et ancrage de celui ci
    Label(aff, text = art.nom).grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
    # Ajout du prix à la fenetre master et ancrage de celui ci
    Label(aff, text = str(art.prix)+" €").grid(row = 2, column = 0, padx = 5, pady = 5)
    # Ajout du nom du site à la fenetre master
    lien = Label(master, text="  "+art.site, cursor="hand2", relief=RAISED)
    # Ancrage de celui ci
    lien.grid(row = 2, column = 1, ipadx = 5, ipady=5)
    # Quand le label est cliqué, cela appelle la fonction hyperlien
    lien.bind("<Button-1>", lambda e:
    hyperlien(art.url))

    # Si ce n'est pas le dernier article
    if ID != len(tri) - 1 :
        # Ajout du bouton permettant de passer au suivant
        suivant = Label(aff, text="  Suivant", cursor="hand2", relief=RAISED)
        # Ancrage de celui ci
        suivant.grid(row = 3, column = 1, ipadx = 5, ipady=5)
        # Quand le label est cliqué, apppel de la fonction fsuivant
        suivant.bind("<Button-1>", lambda e:
        fsuivant(tri))

    # Si ce n'est pas le 1er article
    if ID != 0 :
        # Ajout du bouton permettant de passer au précédent
        precedent = Label(aff, text="  Précédent", cursor="hand2", relief=RAISED)
        # Ancrage de celui ci
        precedent.grid(row = 3, column = 0, ipadx = 5, ipady=5)
        # Quand le label est cliqué, apppel de la fonction fprecedentr
        precedent.bind("<Button-1>", lambda e:
        fprecedent(tri))

    # La fenetre s'active
    aff.mainloop()
