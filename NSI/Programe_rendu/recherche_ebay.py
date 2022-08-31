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
def recherche_ebay(nom_recherche, filtre, driver):
    '''Fonction qui va rechercher des articles sur Ebay
    Prend en parametre:
    - nom de l'article a rechercher
    - filtre (dictionaire des filtres)
    - driver une instance de Selenium
    Qui retourne une liste d'instances de la classe Article
    '''
    # Initialisation de l'url de base
    url = f"https://www.ebay.fr/sch/i.html?_nkw={nom_recherche}"

    if filtre["prixMin"] != -1:
        url += f"&_udlo={filtre['prixMin']}"

    if filtre["prixMax"] != -1:
        url += f"&_udhi={filtre['prixMax']}"

    # filtre achat imediat
    url += "&LH_BIN=1"


    # Nombre de page a visiter
    # nb_page_max <- (filtre["nbArticles"]//60)+1
    nb_page_max = (filtre["nbArticles"]//60)+1

    # page <- 1
    page = 1

    items = []
    
    while page <= nb_page_max:
        driver.get(url+f"&_pgn={page}")
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')

        items += soup.findAll("li",{"class":"s-item s-item__pl-on-bottom"})[1:]

        page += 1



    if len(items) > filtre["nbArticles"]:

        items = items[0:filtre["nbArticles"]]


    liste_temp = []

    for i in items:
        prix = i.find("span",{"class":"s-item__price"}).text
        if "EUR" in prix:
            for j in range(len(prix)):
                if prix[j] == "E":
                    prix = prix[0:j-1]
                    break

        prix = float(prix.replace(",","."))
        
        nom = i.find("h3",{"class":"s-item__title"}).text
        
        url = i.find("a",{"class":"s-item__link"})["href"]
        
        url_img = i.find("img",{"class":"s-item__image-img"})["src"]
        
        site = "Ebay"
        
        liste_temp.append(Article(prix,nom,site,url,url_img))



    return liste_temp























        


    

    

    
