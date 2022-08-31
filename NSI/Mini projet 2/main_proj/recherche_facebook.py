# Contient la fonction rechgerche sur un site
# parametres :
# - nom_recherche : str (article a rechercher)
# - filtres : dict{"prixMin":int,
#                  "prixMax":int,
#                  "nbArticles":int,
#                  ...}
# Renvoir une liste d'instances de la classe Article


# Importation des modules necessaire
# Selenium : pour automatiser un navigateur (est importer dans main.py)

# BeautifulSoup (from bs4) : pour manipuler le code source html d'une page
from bs4 import BeautifulSoup

# time : pour faire des pause lors du chargement des pages
import time
    
# Importation de la classe Article
from classeArticle import Article




# Declaration de la fonction recherche(nom_recherche, filtre, driver)
def recherche_facebook(nom_recherche, filtre, driver):

    # Initialisation de l'url de base
    # url_base <- "https://......" (depend de chaque site)
    url = f'https://m.facebook.com/marketplace//search/?query={nom_recherche}'
    #url = f'https://fr-fr.facebook.com/marketplace/search?minPrice={filtre["prixMin"]}&maxPrice={filtre["prixMax"]}&query={nom_recherche}&exact=false'

    # Ouverture du lien
    driver.get(url)
    
    # Pause 1 sec
    time.sleep(1)


    # Recuperation temporaire du code html de la page
    # html <- driver.page_source
    html = driver.page_source

    # Creation d'une instance temporaire BeautifulSoup
    # soup <- BeautifulSoup(html,'lxml')
    soup = BeautifulSoup(html,'lxml')

    # Recuperation de tout les article avec leur balise et classe html (different pour chaque site)
    # items <- soup.findAll(balise,{"class":nom de la classe})
    
    items = soup.findAll("div",{"class":"_a5o _9_7 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt"})

    # Tant que taille(temp_items) < filtre["nbArticles"]
    while len(items) < filtre["nbArticles"]:

        # longueur_page <- driver.execute_script("return document.body.scrollHeight")
        longueur_page = driver.execute_script("return document.body.scrollHeight")
        
        # Scroll de la page
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Pause 1 sec
        time.sleep(1)
        # nouvelle_longueur_page <- driver.execute_script("return document.body.scrollHeight")
        nouvelle_longueur_page = driver.execute_script("return document.body.scrollHeight")
        
        

        # si longueur_page == nouvelle_longueur_page
        if longueur_page == nouvelle_longueur_page:
            break
            # Plus aucun element a charger
            # sortir de la boucle


        # Recuperation temporaire du code html de la page
        # html <- driver.page_source
        html = driver.page_source

        # Creation d'une instance temporaire BeautifulSoup
        # soup <- BeautifulSoup(html,'lxml')
        soup = BeautifulSoup(html,'lxml')

        # Recuperation de tout les article avec leur balise et classe html (different pour chaque site)
        # items <- soup.findAll(balise,{"class":nom de la classe})
        items = soup.findAll("div",{"class":"_a5o _9_7 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt"})

        # Application du filtre de prix (car non utiliser dans la recherche avec l'url)
        items = [i for i in items if i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[-1] == "€"]
        
        items = [i for i in items if int(i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[0:-2].replace(u"\xa0","")) < filtre["prixMax"] and
                                     int(i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[0:-2].replace(u"\xa0","")) > filtre["prixMin"]]
        
                                    #int(i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[0:-2]) < filtre["prixMax"] and
                                    #int(i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[0:-2]) > filtre["prixMin"]

    # Si taille_items > filtre["nbArticles"]
    if len(items) > filtre["nbArticles"]:
    
        # items <- items[0:filtre["nbArticles"]]
        items = items[0:filtre["nbArticles"]]

    
    # Initialisation de liste_temp
    # liste_temp <- []
    liste_temp = []

    
    # Analyse de chaque items (depend de chaque site)
    # Pour i dans items
    for i in items:

        # Recuperation du prix
        prix = i.find("div",{"class":"_59k _2rgt _1j-f _2rgt"}).text[0:-2].replace(u"\xa0","")

        # Recuperation du nom
        nom = i.find("div",{"class":"_59k _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt"}).text

        # Recuperation de la localisation
        #localisation = i.find("span",{"class":"a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve"}).text
        
        # Recuperation du site
        site = 'Facebook'
        
        # Recuperation de l'url
        url = "https://facebook.com/"+i.find("a")["href"]

        # Recuperation de l'image
        url_img = i.find("img")["src"]

        # Ajout a liste_temp (Article(prix, nom, site, url)
        liste_temp.append(Article(prix,nom,site,url,url_img,None))

    print(len(liste_temp))
    # Return liste_temp
    return liste_temp    




