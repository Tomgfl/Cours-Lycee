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

def recherche_shpock(nom_recherche, filtre, driver):

    # Initialisation de l'url de base
    # url_base <- "https://......" (depend de chaque site)
    url = f'https://www.shpock.com/en-gb/results?q={nom_recherche}'
    if filtre["prixMin"] != -1:
        url += f'&price.from={filtre["prixMin"]}'
        
    if filtre["prixMax"] != -1:
        url += f'&price.to={filtre["prixMax"]}'


    # Initialisation items
    # lst items <- []

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
    items = soup.findAll("a",{"class":"Anchor-sc-1452fce-0 ldbLmI"})
    print(len(items))


    # Si taille_items > filtre["nbArticles"]
    if len(items) > filtre["nbArticles"]:
    
        # items <- items[0:filtre["nbArticles"]]
        items = items[0:filtre["nbArticles"]]

    # Initialisation de liste_temp
    # liste_temp <- []
    liste_temp = []
    

    # print(items[0].findAll("img",{"class":"Image_content__lvAec"}))

    
    # Analyse de chaque items (depend de chaque site)
    # Pour i dans items
    for i in items:
        
        
        # Recuperation du prix
        prix = i.find("p",{"class":"StyledAssets__Title-sc-1ojzb7j-0 ItemCard__Price-sc-cy8zy7-0 cOpshy cdIZhN"}).text

        # Recuperation du nom
        nom = i.find("p",{"class":"StyledAssets__Title-sc-1ojzb7j-0 cOpshy"}).text
        print(nom)
        # Recuperation de la localisation
        #
        
        # Recuperation du site
        site = 'Shpock'
        
        # Recuperation de l'url
        url = i["href"]

        # Recuperation de l'image
        if i.find("img") != None:
            url_img = i.find("img")["src"]
        else:
            url_img = None
        print(url_img)

        # Ajout a liste_temp (Article(prix, nom, site, url)
        liste_temp.append(Article(prix,nom,site,url,url_img,None))
    
    # Return liste_temp
    return liste_temp    