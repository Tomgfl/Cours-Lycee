import sys
sys.path.append("c:\\users\\rabem\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\\localcache\\local-packages\\python39\\site-packages")

# Importation des modules necessaire
# Api
# le bon coin
# vinted ?


# modules necessaire pour webscraping
# requests
import requests

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Importation de la classe Article
from classeArticle import Article

# Importation de chaque modules de recherche( Vinted,...)
from recherche_shpock import recherche_shpock
from recherche_vinted import recherche_vinted
from recherche_ebay import recherche_ebay


# Importation des modules nécessaires
from tkinter import *
from tkinter.ttk import *
from classeArticle import Article
import urllib.request
import webbrowser
import cv2
import numpy as np


# --- Debut du programme ---
def main(nomRechercheArticle,nbArticlesParSites,filtrePrixMini,filtrePrixMax,sites) :



    # filtres <-- dic{"prixMin":filtrePrixMini,
    #                 "prixMax":filtrePrixMax,
    #                 "nbArticles":nbArticlesParSites,
                    
    filtres = {"prixMin":filtrePrixMini,
               "prixMax":filtrePrixMax,
               "nbArticles":nbArticlesParSites}




    # lst allArticles <-- []
    allArticles = []

# Pour chaque site ayant une Api
    # Recherche de nomRechercheArticle avec les filtres

    # Initialisation des variables
    # nbArticles <-- 0
    
    # Tant que nbArticles < nbArticlesParSites ou qu'il n'y a plus d'articles disponibles
        # Creation d'une instance de Article
        # Ajout de cette instance a allArticles
        # nbArticles <-- +1




    # Webscraping sur les sites
                    
    # Initialisation du driver selenium
    # Fichier pour utiliser Chrome
    ser = Service(ChromeDriverManager().install())
                    
    # Option pour chrome
    op = webdriver.ChromeOptions()
                    
    # Option pour que la fenetre ne s'ouvre pas
    op.add_argument('headless')
    op.add_argument('window-size=200x200')
                    
    # driver <- instance selenium webdriver(chrominium)
    driver = webdriver.Chrome(service=ser, options=op)
                    
    if 'shpock' in sites :
        # liste_temp <- recherche_shpock(nomRechercheArticle,filtres,driver)
        liste_temp = recherche_shpock(nomRechercheArticle,filtres,driver)

        # allArticles <- allArticles + liste_temp
        allArticles += liste_temp

    if 'ebay' in sites :
        # liste_temp <- recherche_ebay(nomRechercheArticle,filtres,driver)
        liste_temp = recherche_ebay(nomRechercheArticle,filtres,driver)
                    
        # allArticles <- allArticles + liste_temp
        allArticles += liste_temp

    if 'vinted' in sites :
        liste_temp = recherche_vinted(nomRechercheArticle,filtres,driver)
        allArticles += liste_temp

# A faire pour chaque fonction recherche
#...
#...

# Fermer Chrome
    driver.quit()



# Affichage des resulatat trier par ordre croissant ( algo_affichage )



# Initialisation liste trier
# Liste_trier <- []

# Tant que allArticles est non vide
    # plus petit prix <- prix premier article
    # mini <- allArticles[0].prix
    
    # article le moins chere <- premier article
    # art <- allArticles[0]
    
    # identifient de l'article
    # id_art <- 0
    
    # Pour i parcourant allArticles
        # Si i.prix < mini
            # mini <- allArticles[i].prix
            # art <- allArticles[i]
            # id_art <- i
            
    # Ajout a Liste_trier (article)
    # Supression de l'article



    trier = []
    while allArticles:
        mini = allArticles[0].prix
        art = allArticles[0]
        id_art = 0
        for i in range(len(allArticles)):
            if allArticles[i].prix < mini:
                mini = allArticles[i].prix
                art = allArticles[i]
                id_art = i
        trier.append(art)
        allArticles.pop(id_art)

    affiche(tri)
    





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
    motrecherche=recherche.get()
    prixmin = pmin.get()
    prixmax= pmax.get()
    nombrearticle= nbart.get()
    sites = []
    if shpock.get():
        sites.append("shpock")
    if ebay.get() :
        sites.append("ebay")
    if vint.get():
        sites.append("vinted")
    main(motrecherche,nombrearticle,prixmin,prixmax,sites)

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
shpock = IntVar()
# Création de la case à cocher qui correspond à la variable face
sh = Checkbutton(master, text="Shpock",variable = shpock)
# Ancrage de celle-ci
sh.grid(row = 1, column = 3,padx = 10, pady = 5, sticky = W)

# Initialisation de la variable entière topa
ebay = IntVar()
# Création de la case à cocher qui correspond à la variable topa
eb = Checkbutton(master, text="Ebay",variable = ebay)
# Ancrage de celle-ci
eb.grid(row = 2, column = 3, pady = 5,padx = 10, sticky = W)

master.mainloop()

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

    # Si il y a une image liée à l'annonce
    if art.url_img != None :
        # Téléchargement de l'image de l'annonce
        urllib.request.urlretrieve(art.url_img,art.nom+".png")
        # Chargement de cette image dans la variable img de classe cv2.imread
        img = cv2.imread(art.nom+".png")
        # Chargement de l'image redimensionnée dans la variable res
        res = cv2.resize(img, dsize=(200,300), interpolation=cv2.INTER_CUBIC)
        # Enregistrement de l'image redimensionnée
        cv2.imwrite(art.nom+".png", res)

        # Chargement de l'image redimensionnée dans la variable img de classe PhotoImage
        img = PhotoImage(file = art.nom +".png")
        # Ajout de cette image à la fenetre master et ancrage de celle ci
        Label(aff, image = img).grid(row = 0, column = 0,columnspan = 2, rowspan = 1, padx = 5, pady = 5)

    # Ajout du nom à la fenetre master et ancrage de celui ci
    Label(aff, text = art.nom).grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
    # Ajout du prix à la fenetre master et ancrage de celui ci
    Label(aff, text = str(art.prix)+" €").grid(row = 2, column = 0, padx = 5, pady = 5)
    # Ajout du nom du site à la fenetre master
    lien = Label(aff, text="  "+art.site, cursor="hand2", relief=RAISED)
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













        

    
