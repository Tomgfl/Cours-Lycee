# Nom du fichier : classeArticle.py
# Création de la classe Article contenant les attribut prix, site, url et localisation pour chaque instance.
class Article:

    # définition de la méthode __init__(self,Prix,Nom,Site,Url,Localisation)
    def __init__(self,Prix,Nom,Site,Url,Url_img,Localisation):
        
        # self.prix <-- Prix
        self.prix = Prix

        #self.nom <-- Nom
        self.nom = Nom
        
        # self.site <-- Site
        self.site = Site
        
        # self.url <-- Url
        self.url = Url
        
        # self.url_img <-- Url_img
        self.url_img = Url_img
        
        # self.localisation <-- Localisation
        self.localisation = Localisation
