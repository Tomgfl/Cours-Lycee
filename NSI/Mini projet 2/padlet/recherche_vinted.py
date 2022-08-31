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
def recherche_vinted(nom_recherche, filtre, driver):

    # Initialisation de l'url de base
    # url_base <- "https://......" (depend de chaque site)
    url = f'https://www.vinted.fr/vetements?search_text={nom_recherche}'
    if filtre["prixMin"] != -1:
        url += f'&price_from={filtre["prixMin"]}'
        
    if filtre["prixMax"] != -1:
        url += f'&price_to={filtre["prixMax"]}'

    # Nombre de page a visiter
    nb_page_max = (filtre["nbArticles"]//24)+1
    
    # Initialisation de la page actuelle
    page = 1

    # Initialisation items
    # lst items <- []
    items = []
    
    # Tant que la nombre de page total n'est pas visiter
    # Tant que page <= nb_page_max
    while page <= nb_page_max:
        
        # Ouverture du lien
        driver.get(url+f"&page={page}")
        
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
        items_temp = soup.findAll("div",{"class":"feed-grid__item"})
        # Supression des anonces non voulues
        del items_temp[6]
        
        items += items_temp
        print(len(items))
        
        # Incrementation page
        page += 1


    # Si taille_items > filtre["nbArticles"]
    if len(items) > filtre["nbArticles"]:
    
        # items <- items[0:filtre["nbArticles"]]
        items = items[0:filtre["nbArticles"]]

    
    # Initialisation de liste_temp
    # liste_temp <- []
    liste_temp = []

    print(items[0].findAll("img",{"class":"Image_content__lvAec"}))

    
    # Analyse de chaque items (depend de chaque site)
    # Pour i dans items
    for i in items:
        
        #for j in range(len(i.text)):
        #    if i.text[j] == '€':
        #        prix = int(i.text[0:j-1])
        #        nom = i.text[j+1:]


        # Recuperation du prix
        prix = i.find("h3",{"class":"Text_text__QBn4- Text_subtitle__1I9iB Text_left__3s3CR Text_amplified__2ccjx Text_bold__1scEZ"}).text[0:-2]

        # Recuperation du nom
        
        nom = i.findAll("img",{"class":"Image_content__lvAec"})[1]["alt"]
        print(nom)
        # Recuperation de la localisation
        #
        
        # Recuperation du site
        site = 'Vinted'
        
        # Recuperation de l'url
        url = i.find("a",{"class":"ItemBox_overlay__1kNfX"})["href"]

        # Recuperation de l'image
        url_img = i.findAll("img",{"class","Image_content__lvAec"})[1]["src"]

        # Ajout a liste_temp (Article(prix, nom, site, url)
        liste_temp.append(Article(prix,nom,site,url,url_img,None))
    
    # Return liste_temp
    return liste_temp    




