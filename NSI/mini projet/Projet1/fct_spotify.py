import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# ID pour la connexion a l'API de spotify

s_client_id = '3a17d9f8c1014f198c91d214ec31aa07'
s_client_secret = '0b4f9e9ef27e485db92beeaf75d47f0a'
s_redirect_url = 'http://127.0.0.1:5000/callback.html' #'https://google.fr'


def connexion_spotify():
    """Connexion au compte Spotify"""

    # Supression du cache (deconexion du compte)

    if os.path.exists(".cache"):
        os.remove(".cache")
    
    # Affichage pour l'utilisateur
    print(
        "Vous allez etre regiriger vers spotify pour vous connecter a votre compte.\n"
        "Puis colle le lien vers lequel vous avez ete rediriger.\n")
    a = input("Appuyer sur 'Entrer' pour continuer.")

    # Ce que le programme a le droit d'utiliser 
    scope = ("playlist-modify-private", "playlist-read-private", "playlist-modify-public", "playlist-read-collaborative")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(s_client_id, s_client_secret, s_redirect_url, scope=scope))

    # Affichage utilisateur
    user = sp.current_user()
    print(f"Connecter en tant que l'utilisateur :{user['display_name']}")
    print()
    return sp


def recuperation_playliste_spotify(sp):
    """ Recupere et retourne le playliste a convertire"""
    
    # recuperation de toutes les donnee sur les playlistes de l'utilisateur
    playlists = sp.current_user_playlists()

    # liste qui va contenir tous les noms et id de toutes les playlistes de l'utilisateur
    liste_playlist = [(items['name'], items['uri']) for items in playlists['items']]

    # Affichage de toutes les playlistes avec un numero a selectioner
    for i in range(len(liste_playlist)):
        print(f"{i + 1} : {liste_playlist[i][0]}")

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
            liste_playlist[choix - 1]
            assert choix > 0

            # Validation de la boucle while
            playlists_selectionner = True

        # Si une erreur est trouver
        except :
            print("ERREUR : Veuillez saisir un ID valide\n")

    # Affichage utilisateur
    print(f"Vous avez selectionner la playlist : {liste_playlist[(choix - 1)][0]}\n")

    # Creation de la liste qui va contenir les noms des [(sons,albums,artistes)]
    liste_sons = []
    for i in sp.playlist(liste_playlist[choix-1][1])['tracks']['items']:
        liste_sons.append((i['track']['name'], i['track']['album']['name'], i['track']['artists'][0]['name']))
        #print(i['track']['name'])
        #print(f"album : {i['track']['album']['name']}")
        #print(f"artiste : {i['track']['artists'][0]['name']}")
        #print()

    #print(len(sp.playlist(liste_playlist[choix-1][1])['tracks']['items']))
    #print(liste_sons)
    return liste_sons


def creation_playlist(sp,playlist):
    #playlist sous forme de lst[(sons,album,artiste),(sons,album,artiste)...]

    # Recuperation clavier du nom de la playlist
    nom = input("Nom de la playlist : ")
    
    id_user = sp.current_user()["id"]
    
    # Creation de la playlist
    playlist_create = sp.user_playlist_create(id_user,nom,False)
    
    # Creation de la liste contenent les ID des sons a ajouter a la playlist
    list_id = []
    
    # Recherche de chaque titre et recuperation de son ID
    for item in playlist:
        id_son = sp.search(item[0],1)["tracks"]["items"][0]["id"]
        list_id.append(id_son)
    
    # Ajout de chaque titre a la playlist
    sp.playlist_add_items(playlist_create["id"],list_id)
    print("playlist cree avec succes !")

    


#sp = connexion_spotify()
#a_convertir = recuperation_playliste_spotify(sp)
#creation_playlist(sp,a_convertir)

