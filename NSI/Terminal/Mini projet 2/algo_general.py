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

# Recuperation du nombre d'aticles a rechercher par site
# Tant que Vrai
    # Essay
        # nbArticlesParSites <-- int entree clavier utilisateur
    # Si une erreur:
        # Affichage ecran("Veillez entree un entier")
    
    # Si nbArticlesParSites > 0 et < 1000
        # Affichage ecran ("Vous souhaitez charcher {nbArticlesParSites} par site")
        
        # Sortir de la boucle
    
    # Sinon
        # Affichage ecran ("Erreur : La valeur doit etre positive et inferieur a 1000")
        

# Recuperation du prix minimum
# Tant que Vrai
    # Essay
        # filtrePrixMini <-- int entree clavier utilisateur (-1 for none)
    # Si  erreur
        # Affichage ecran ("Veillez entree un entier")
        
    # Si filtrePrixMini = -1 ou filtrePrixMini > 0:
        # Affichage ecran ("Prix minimum : {filtrePrixMini}")
        
        # Sortir de la boucle
        
    # Sinon 
        # Affichage ecran ("Erreur : La valeur doit etre positive")
    
    
# Recuperation du prix max
# Tant que Vrai
    # Essay
        # filtrePrixMax <-- int entree clavier utilisateur (-1 for none)
    # Si  erreur
        # Affichage ecran ("Veillez entree un entier")
        
    # Si filtrePrixMax = -1 ou filtrePrixaMax > 0:
        # Affichage ecran ("Prix minimum : {filtrePrixMax}")
        
        # Sortir de la boucle
        
    # Sinon 
        # Affichage ecran ("Erreur : La valeur doit etre positive")
        



# filtres <-- dic{"prixMin":flitrePrixMini,
#                 "prixMax":flitrePrixMax,
#                 "nbArticles":nbArticlesParSites}




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




















        
