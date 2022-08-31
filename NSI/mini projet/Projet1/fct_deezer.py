import deezersdk    #A installer : pip install deezersdk
import webbrowser   #A installer : pip install webbrowser
import deezer
import requests

#Les ID pour l'API de deezer
ID_APP = "511402"
REDIRECT_URL = "https://www.google.com/"
APP_SECRET = "ac2c61e0776e31a4541f6ea7336c76c9"

def connexion_deezer():
    """Connexion au compte Deezer"""

    # Affichage pour l'utilisateur
    print(
        "Vous allez etre regiriger vers deezer pour vous connecter a votre compte.\n"
        "Puis colle le lien vers lequel vous avez ete rediriger.\n")
    a = input("Appuyer sur 'Entrer' pour continuer.")
    
    #lien pour se connecter au compte
    link = f'https://connect.deezer.com/oauth/auth.php?app_id={ID_APP}&redirect_uri={REDIRECT_URL}&perms=basic_access,manage_library'

    #Ouverture du navigateur pour se connecter au compte
    webbrowser.open(link)

    CODE = input("Collez le lien vers lequel vous avez ete rediriger apres votre connection :")
    CODE = CODE[29:]

    #Recuperation du token de connection
    TOKEN = deezersdk.deezersdk.Deezer.get_oauth_token(ID_APP, APP_SECRET, CODE)

    dz = deezersdk.deezersdk.Deezer(app_id = ID_APP, token = TOKEN)

    #client pour utiliser les fonctions de l'API deezer
    client = deezer.Client(app_id = ID_APP, app_secret = APP_SECRET)
    
    return dz,client

def recuperation_playlist_deezer(dz,client):
    """ Recupere et retourne le playliste a convertir"""

    #Recuperations des playlist de l'utilisateur
    playlists = dz.get_my_playlists()

    # Affichage de toutes les playlistes avec un numero a selectioner
    for i in range(len(playlists)):
        print(f"{i+1} : {playlists[i].title}")

    # Selection de la playliste
    playlists_selectionner = False
    while playlists_selectionner == False:

        # Recuperation clavier du numero de la playlist a selectioner
        choix = input("Veuillez choisir la playlist a selectioner : ")
        
        # Verification que le choix soit valide
        try:
            # Verification que la saisie est un nombre
            choix = int(choix)

            # Verification que la saisie est dans les valeurs possibles
            playlists[choix - 1]
            assert choix > 0

            # Validation de la boucle while
            playlists_selectionner = True
            
        # Si une erreur est trouver
        except :
            print("ERREUR : Veuillez saisir un ID valide\n")


    # Affichage utilisateur   
    print(f"Vous avez selectionner la playlist : {playlists[choix - 1].title}\n")

    # Recuperation des infos de la playlist
    playlist_select = client.get_playlist(playlists[choix-1].id_)
    playlist_select = playlist_select.get_tracks()
    
    # Creation de la liste qui va contenir les noms des [(sons,albums,artistes)]
    liste_sons = []

    for i in range(len(playlist_select)):
        liste_sons.append((playlist_select[i].title,playlist_select[i].album.title,playlist_select[i].artist.name))
        #print(playlist_select[i].title)
        #print(playlist_select[i].album.title)
        #print(playlist_select[i].artist.name)
        #print()

    return liste_sons

def creation_playlist(dz,client,playlist):

    # Recuperation clavier du nom de la playlist
    nom = input("Nom de la playlist : ")

    # Creation de la playlist 
    playlist_create = requests.post(f"https://api.deezer.com/user/me/playlists?title={nom}&access_token={dz.access_token}")

    # Recuperation de l'ID de la playlist cree 
    id_playlist_create = playlist_create.text[6:-1]

    # Creation de la liste contenent les ID des sons a ajouter a la playlist
    list_id = []

    # Recherche de chaque titre et recuperation de son ID
    for item in playlist:

        # Recuperation de l'ID
        track = client.search(item[0],limit = 1)

        # Ajout du titre a la playlist
        requests.post(f'https://api.deezer.com/playlist/{id_playlist_create}/tracks?songs={track[0].id}&access_token={dz.access_token}')
    
    print("playlist cree avec succes !")
    
    #requests.post(f'https://api.deezer.com/playlist/9655552382/tracks?songs=3135556&access_token={dz.access_token}')
        
#dz, client = connexion_deezer()
#a_convertir = recuperation_playlist_deezer(dz,client)
#creation_playlist(dz,client,a_convertir)
#print(a_convertir)




