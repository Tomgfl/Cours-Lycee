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
#nomRechercheArticle = input("Nom de l'article a rechercher : ") 

# nbArticlesParSites <-- int entree clavier utilisateur
#nbArticlesParSites = int(input("Nombres d'articles max a recuperer sur chaque site : "))

# filtrePrixMini <-- int entree clavier utilisateur (-1 for none)
#filtrePrixMini = int(input("Prix minimum (-1 pour None) : "))

# filtrePrixMax <-- int entree clavier utilisateur (-1 for none)
#filtrePrixMax = int(input("Prix maximum (-1 pour None) : "))

# ? filtreLocalisation <-- str entree clavier utilisateur (-1 for none)



# filtres <-- dic{"prixMin":filtrePrixMini,
#                 "prixMax":filtrePrixMax,
#                 "nbArticles":nbArticlesParSites}
                    


def main_recherche(nomRechercheArticle,nbArticlesParSites,filtrePrixMini,filtrePrixMax,sites):
    '''Fonction qui prend en parametre:
    - le nom de l'article rechercher
    - le nombre d'articles a rechercher par site
    - le prix minimum
    - le prix maximum
    - une liste des sites sur lesquelles chercher les articles
    Qui revoie une liste trier d'instances de la classe Articles trier par ordre croissant de prix
    '''
    
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
    # extention pour empecher les images de charger pour que les pages chargent plus rapidement
    op.add_extension("Block-image.crx")
                    
    # Option pour que la fenetre ne s'ouvre pas(bug quand c'est activé)
    #op.add_argument('headless')
    #op.add_argument('window-size=200x200')
                    
    # driver <- instance selenium webdriver(chrominium)
    driver = webdriver.Chrome(service=ser, options=op)
                    

    # liste_temp <- recherche_facebook(nomRechercheArticle,filtres,driver)
    ###liste_temp = recherche_facebook(nomRechercheArticle,filtres,driver)
                    
    # allArticles <- allArticles + liste_temp
    ###allArticles += liste_temp
    
    if 'vinted' in sites:
        allArticles += recherche_vinted(nomRechercheArticle,filtres,driver)
    if 'ebay' in sites:
        allArticles += recherche_ebay(nomRechercheArticle,filtres,driver)
    if 'shpock' in sites:
        allArticles += recherche_shpock(nomRechercheArticle,filtres,driver)

    # A faire pour chaque fonction recherche
    #...
    #...

    # Fermer Chrome
    driver.quit()


    # Affichage des resulatat trier par ordre croissant ( algo_affichage )

    # trie de la liste
    trier = trie_lst(allArticles)

    # renvoie la liste trier
    return trier
    
    

def trie_lst(lst_articles):

    trier = []
    while lst_articles:
        mini = lst_articles[0].prix
        art = lst_articles[0]
        id_art = 0
        for i in range(len(lst_articles)):
            if lst_articles[i].prix < mini:
                mini = lst_articles[i].prix
                art = lst_articles[i]
                id_art = i
        trier.append(art)
        lst_articles.pop(id_art)
    
    return trier

















        
