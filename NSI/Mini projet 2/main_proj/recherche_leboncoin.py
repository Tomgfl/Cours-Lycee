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


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Declaration de la fonction recherche(nom_recherche, filtre, driver)
def recherche_lbc(nom_recherche, filtre, driver):

    # Initialisation de l'url de base
    # url_base <- "https://......" (depend de chaque site)
    url = "https://www.proxysite.com/"
    #url = f'https://fr-fr.facebook.com/marketplace/search?minPrice={filtre["prixMin"]}&maxPrice={filtre["prixMax"]}&query={nom_recherche}&exact=false'

    # Ouverture du lien
    driver.get(url)
    
    # Pause 1 sec
    time.sleep(1)

    # base de l'url
    url = f"https://www.leboncoin.fr/recherche?text={nom_recherche}&price="
    # filtre prix minimum
    if filtre["prixMin"] != -1:
        url += str(filtre["prixMin"])
    else:
        url += "min"
    url += "-"
    # filtres prix maximum
    if filtre["prixMax"] != -1:
        url += str(filtre["prixMax"])
    else:
        url += "max"
    # page 1
    page = 1

    # Nombre de page a visiter
    nb_page_max = (filtre["nbArticles"]//35)+1

    
    
    all_proxy = ["us1","eu1","eu2","us2","eu3","us3","eu4","us4","eu5","us5",
                 "eu6","us6","eu7","us7","eu8","us8","eu9","us9","eu10","us10",
                 "eu11","us11","eu12","us12","eu13","us13","eu14","us14","eu15","us15",
                 "eu16","us16","eu17","us17","eu18"]
    
    while all_proxy:

        # selection du proxy
        l = Select(driver.find_element_by_name("server-option"))
        l.select_by_value(all_proxy[0])
        

        # recherche du lien
        s = driver.find_element_by_name("d")
        s.clear()
        time.sleep(1)
        s.send_keys(url+f"&page={page}")
        s.send_keys(Keys.ENTER)

        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')
        
        if soup.find("div",{"class":"alert alert-danger"}):
            del all_proxy[0] 
        else:
            prox = all_proxy[0]
            break

    items = []

    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    items += soup.findAll("div",{"class":"styles_adCard__HQRFN styles_classified__rnsg4"})

    
    for i in range(2,nb_page_max+1):
    
        s = driver.find_element_by_name("d")
        s.clear()
        time.sleep(1)
        s.send_keys(url+f"&page={i}")
        s.send_keys(Keys.ENTER)

        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')

        items += soup.findAll("div",{"class":"styles_adCard__HQRFN styles_classified__rnsg4"})
        

        time.sleep(1)
    
    
    print(len(items))
    
    liste_temp = []

    for i in items:

        prix = i.find("span",{"class":"_137P- P4PEa _35DXM"}).text
        prix = float(prix[:-2])
        
        nom = i.find("p",{"data-qa-id":"aditem_title"}).text

        site = "le bon coin"
        
        url = "https://"+prox+".proxysite.com"+i.find("a")["href"]

        #url_img = i.find("source",{"type":"image/jpeg","media":"(min-width: 480px)"})["srcset"]
    
        
        liste_temp.append(Article(prix,nom,site,url,None,None))
        
    return liste_temp   











