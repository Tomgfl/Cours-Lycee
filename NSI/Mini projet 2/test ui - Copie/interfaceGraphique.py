# Importation des modules necessaires
from tkinter import *
from tkinter.ttk import *
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from urllib.request import urlopen
from io import BytesIO
import webbrowser
from functools import partial
import requests

from main_recherche import *


# Initialisation de la fenetre
master = Tk()

#Creation de la zone pour tous les articles
Frame_allArticles = Frame(master)
Frame_allArticles.grid(row=1,column=0,sticky=W)


Frame_filtres = Frame(master)
Frame_filtres.grid(row=0,column=0,sticky=W)
                   
# Création de la zone de texte 1
label1= Label(Frame_filtres, text="Entrez votre recherche :")
# Ancrage de la zone de texte 1
label1.grid(row=0, column=0,padx=5,pady=5)

# Création de la barre de recherche
recherche = Entry(Frame_filtres)
# Ancrage de la barre de recherche
recherche.grid(row = 1, column = 0, sticky = W, pady = 2,padx=5) 


def print_item(article,ID):
    '''Fonction qui prend en parametre:
    - une instance de la class article
    - un ID de positionnement
    
    et qui affiche dans la fenetre:
    - l'image de l'articles
    - son nom
    - son prix'''
    
    #Recuperation de la frame global pour tous les articles
    global Frame_allArticles

    #placement (max 15 articles par ligne)
    ID_x = ID%15
    ID_y = ID//15

    #frame
    Frame_article = Frame(Frame_allArticles)

    #image
    #Ouverture de la photo
    photo = open_from_url(article.url_img)
    #Label image
    Label_image = Label(Frame_article, image=photo)
    Label_image.photo = photo
    Label_image.grid(row=0, column=0)

    #nom
    #Si le nom est trop long
    if len(article.nom) > 15:
        #Reduire le nom
        nom = article.nom[0:13]+'...'
    else:
        nom = article.nom
    #Label texte du nom
    Label_text_nom = Label(Frame_article, text=nom)
    Label_text_nom.grid(row=1, column=0, sticky = W)

    #Label texte du prix
    Label_text_prix = Label(Frame_article, text=str(article.prix)+' €')
    Label_text_prix.grid(row=2, column=0, sticky = W)

    #Label texte nom du site
    Label_text_site = Label(Frame_article, text=article.site)
    Label_text_site.grid(row=3, column=0, sticky = W)

    #Label bouton lien
    #Bouton pour ouvrir le lien de l'aricle dans le navigateur 
    Label_button = Button(Frame_article,text="Ouvrir",command=partial(open_browser,article.url))
    Label_button.grid(row=4,column=0,sticky = W)

    # encrage de la frame de l'article en fonction de son ID
    Frame_article.grid(row=3+ID_y, column=ID_x, sticky = W)

    
def open_browser(url):
    '''Fonction qui prend en parametre l'url d'un article et qui l'ouvre dans un navigateur internet '''
    #Ouverture du lien
    webbrowser.open(url)

def open_from_url(url):
    '''Fonction qui prend en parametre l'url d'une image et qui permet de l'afficher sur l'interface graphique'''
    #print(url)
    try:
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        im_resize = im.resize((100,120))
        photo = ImageTk.PhotoImage(im_resize)

        #u = urlopen(url,timeout=5)
        #raw_data = u.read()
        #u.close()
        #im = Image.open(BytesIO(raw_data))
        
    # si l'image n'a pas pu etre ouverte
    except:
        # ouverture d'une image vide
        im = Image.open("Image_vide.png")
        photo = ImageTk.PhotoImage(im)
        
    return photo

# Définition de la fonction recupere() qui récupère les valeurs de toutes les entrées et les attribue aux variables liées
def recupere():
    '''Fonction qui va:
    - recuperer les filtres
    - effectuer la recherche avec les filtres
    - afficher tous les articles
    '''
    # Recuperation des filtres
    # Recuperation du nom de l'article a chercher
    motrecherche=recherche.get()
    # Recuperation du prix mini
    prixmin = int(pmin.get())
    # Recuperation du prix max
    prixmax= int(pmax.get())
    # Recuperation du nombre d'articles
    nombrearticle= int(nbart.get())

    # Initialisation des sites a parcourir
    # sites -> []
    sites = []

    # Si la case shpock est cocher 
    if shpock.get():
        # Ajouter "shpock" a la liste
        sites.append("shpock")
    # Si la case ebay est cocher 
    if ebay.get() :
        # Ajouter "ebay" a la liste
        sites.append("ebay")
    # Si la case vinted est cocher 
    if vint.get():
        # Ajouter "vinted" a la liste
        sites.append("vinted")

    # Recuperation des articles
    # Appel de la fonction main_recherche
    allArticles = main_recherche(motrecherche,nombrearticle,prixmin,prixmax,sites)
    
    # Pour i parcourant allArticles
    for i in range(len(allArticles)):
        # Affichage de l'article
        print_item(allArticles[i],i)


    

# Création du bouton valider qui déclenche la fonction recupere
bouton = Button(Frame_filtres, text="Valider", command=recupere)
# Ancrage du bouton
bouton.grid(row = 2,column = 0, sticky = W, pady= 2, padx=27)

# Création de la zone de texte 2
label2 = Label(Frame_filtres, text= "Prix minimum :")
# Ancrage de la zone de texte 2
label2.grid(row = 0, column = 1,sticky = E, pady=5)

# Création de l'entrée du prix minimal
pmin = Spinbox(Frame_filtres,width=7,from_=0,to=10000)
# Ancrage de celle ci
pmin.grid(row = 0, column= 2, pady= 5)

# Création de la zone de texte 3
label3 = Label(Frame_filtres, text= "Prix maximum :")
# Ancrage de la zone de texte 3
label3.grid(row = 1, column = 1,sticky = E, pady=5)

# Création de l'entrée du prix minimal
pmax = Spinbox(Frame_filtres,width=7,from_=0,to=10000)
# Ancrage de celle-ci
pmax.grid(row = 1, column= 2, pady= 5)

# Création de la zone de texte 4
label4 = Label(Frame_filtres, text= "Nombre d'articles par site :")
# Ancrage de la zone de texte 4
label4.grid(row = 2, column = 1, pady=5)

# Création de l'entrée du nombre d'articles par site
nbart = Spinbox(Frame_filtres,width=7,from_=1,to=10000)
# Ancrage de celle-ci
nbart.grid(row = 2, column= 2, pady= 5)

# Initialisation de la variable entière vint
vint= IntVar()
# Création de la case à cocher qui correspond à la variable vint
vt = Checkbutton(Frame_filtres, text="Vinted",variable = vint)
# Ancrage de celle-ci
vt.grid(row = 0, column = 3, pady = 5,padx = 10, sticky = W)

# Initialisation de la variable entière face
shpock = IntVar()
# Création de la case à cocher qui correspond à la variable face
sh = Checkbutton(Frame_filtres, text="Shpock",variable = shpock)
# Ancrage de celle-ci
sh.grid(row = 1, column = 3,padx = 10, pady = 5, sticky = W)

# Initialisation de la variable entière topa
ebay = IntVar()
# Création de la case à cocher qui correspond à la variable topa
eb = Checkbutton(Frame_filtres, text="Ebay",variable = ebay)
# Ancrage de celle-ci
eb.grid(row = 2, column = 3, pady = 5,padx = 10, sticky = W)

master.mainloop()



























    
    
    
    




