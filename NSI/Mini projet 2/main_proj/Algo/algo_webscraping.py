# Contient la fonction rechgerche sur un site
# parametres :
# - nom_recherche : str (article a rechercher)
# - filtres : dict{"prixMin":int,
#                  "prixMax":int,
#                  "nbArticles":int,
#                  ...}
# Renvoir une liste d'instances de la classe Article


# Importation des modules necessaire
# Selenium : pour automatiser un navigateur
# BeautifulSoup (from bs4) : pour manipuler le code source html d'une page
# time : pour faire des pause lors du chargement des pages
    
# Importation de la classe Article



# Initialisation de selenium

# driver <- instance selenuim


# Declaration de la fonction recherche(nom_recherche, filtres, driver)

    # Initialisation de l'url de base
    # url_base <- "https://......" (depend de chaque site)

    # url de la recherche
    # url <- url_base + nom_recherche + filtre (syntaxe differentes pour chaque site)


    # Ouverture du lien
    # driver.get(url)
    
    # Pause 1 sec


    # Recuperation temporaire du code html de la page
    # html <- driver.page_source

    # Creation d'une instance temporaire BeautifulSoup
    # soup <- BeautifulSoup(html,'lxml')

    # Recuperation de tout les article avec leur balise et classe html (different pour chaque site)
    # items <- soup.findAll(balise,{"class":nom de la classe})


    # Tant que taille(temp_items) < filtre["nbArticles"]
        
        # longueur_page <- driver.execute_script("return document.body.scrollHeight")
        # Scroll de la page
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # nouvelle_longueur_page <- driver.execute_script("return document.body.scrollHeight")
        # Pause 1 sec

        # si longueur_page == nouvelle_longueur_page
            # Plus aucun element a charger
            # sortir de la boucle


        # Recuperation temporaire du code html de la page
        # html <- driver.page_source

        # Creation d'une instance temporaire BeautifulSoup
        # soup <- BeautifulSoup(html,'lxml')

        # Recuperation de tout les article avec leur balise et classe html (different pour chaque site)
        # items <- soup.findAll(balise,{"class":nom de la classe})


    # Si taille_items > filtre["nbArticles"]
    
        # items <- items[0:filtre["nbArticles"]]


    # Initialisation de liste_temp
    # liste_temp <- []

    # Analyse de chaque items (depend de chaque site)
    # Pour i dans items

        # Recuperation du prix
        # Recuperation du nom
        # Recuperation du site
        # Recuperation de l'url


        # Ajout a liste_temp (Article(prix, nom, site, url)


    # Return liste_temp
        





