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
    '''Fonction qui va rechercher des articles sur shpock
    Prend en parametre:
    - nom de l'article a rechercher
    - filtre (dictionaire des filtres)
    - driver une instance de Selenium
    Qui retourne une liste d'instances de la classe Article
    '''
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
        # Conversion en type -> float
        
        try:
            prix = float(prix[1:])
        except:
            if "CHF" in prix:
                prix = float(prix[3:])
            else:
                prix = prix[1:]
                for j in range(len(prix)):
                    if prix[j] == '€':
                        prix = float(prix[0:j-1])
                        break
        
        # Recuperation du nom
        nom = i.find("p",{"class":"StyledAssets__Title-sc-1ojzb7j-0 cOpshy"}).text
        
        # Recuperation du site
        site = 'Shpock'
        
        # Recuperation de l'url
        url = "https://www.shpock.com"+i["href"]

        # Recuperation de l'image
        if i.find("img") != None:
            url_img = i.find("img")["src"]
        else:
            url_img = None
        #print(url_img)

        # Ajout a liste_temp (Article(prix, nom, site, url, url_img)
        liste_temp.append(Article(prix,nom,site,url,url_img))
    
    # Return liste_temp
    return liste_temp    
