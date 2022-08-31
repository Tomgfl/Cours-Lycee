# Importation des modules necessaire
# Api
# le bon coin
# vinted ?

# modules necessaire pour webscraping
# requests
# selenium
# bs4 ( import Beautifulsoup )


# Importation de la classe Article

# Importation de chaque modules de recherche( Facebook,...)



# --- Debut du programme ---

# Entree clavier 
# nomRechercheArticle <-- str entree clavier utilisateur

# nbArticlesParSites <-- int entree clavier utilisateur

# filtrePrixMini <-- int entree clavier utilisateur (-1 for none)

# filtrePrixMax <-- int entree clavier utilisateur (-1 for none)

# ? filtreLocalisation <-- str entree clavier utilisateur (-1 for none)



# filtres <-- dic{"prixMin":flitrePrixMini,
#                 "prixMax":flitrePrixMax,
#                 "nbArticles":nbArticlesParSites,
#                 "localisation":filtreLocalisation}




# lst allArticles <-- []

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

# driver <- instance selenium webdriver(chrominium)


# liste_temp <- recherche_facebook(nomRechercheArticle,filtres,driver)
# allArticles <- allArticles + liste_temp

# A faire pour chaque fonction recherche
#...
#...





# Affichage des resulatat trier par ordre croissant ( algo_affichage )




















        
