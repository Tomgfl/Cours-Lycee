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

# Importation de chaque modules de recherche( Facebook,...)
#from recherche_facebook import recherche_facebook
from recherche_vinted import recherche_vinted
from recherche_ebay import recherche_ebay
from recherche_shpock import recherche_shpock


# --- Debut du programme ---

# Entree clavier 
# nomRechercheArticle <-- str entree clavier utilisateur
nomRechercheArticle = input("Nom de l'article a rechercher : ") 

# nbArticlesParSites <-- int entree clavier utilisateur
nbArticlesParSites = int(input("Nombres d'articles max a recuperer sur chaque site : "))

# filtrePrixMini <-- int entree clavier utilisateur (-1 for none)
filtrePrixMini = int(input("Prix minimum (-1 pour None) : "))

# filtrePrixMax <-- int entree clavier utilisateur (-1 for none)
filtrePrixMax = int(input("Prix maximum (-1 pour None) : "))

# ? filtreLocalisation <-- str entree clavier utilisateur (-1 for none)



# filtres <-- dic{"prixMin":filtrePrixMini,
#                 "prixMax":filtrePrixMax,
#                 "nbArticles":nbArticlesParSites,
#                 "localisation":filtreLocalisation}
                    
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
op.add_extension("Block-image.crx")
                    
# Option pour que la fenetre ne s'ouvre pas
op.add_argument('headless')
op.add_argument('window-size=200x200')
                    
# driver <- instance selenium webdriver(chrominium)
driver = webdriver.Chrome(service=ser, options=op)
                    

# liste_temp <- recherche_facebook(nomRechercheArticle,filtres,driver)
###liste_temp = recherche_facebook(nomRechercheArticle,filtres,driver)
                    
# allArticles <- allArticles + liste_temp
###allArticles += liste_temp

#allArticles += recherche_vinted(nomRechercheArticle,filtres,driver)

#allArticles += recherche_ebay(nomRechercheArticle,filtres,driver)

allArticles += recherche_shpock(nomRechercheArticle,filtres,driver)

# A faire pour chaque fonction recherche
#...
#...

# Fermer Chrome
#driver.quit()



# Affichage des resulatat trier par ordre croissant ( algo_affichage )

save = list(allArticles)
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

















        
