# Initialisation liste trier
# Liste_trier <- []

# Tant que allArticles est non vide
    # plus petit prix <- prix premier article
    # mini <- allArticles[0].prix
    
    # article le moins chere <- premier article
    # art <- allArticles[0]
    
    # identifient de l'article
    # id_art <- 0
    
    # Pour i parcourant allArticles
        # Si i.prix < mini
            # mini <- allArticles[i].prix
            # art <- allArticles[i]
            # id_art <- i
            
    # Ajout a Liste_trier (article)
    # Supression de l'article


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