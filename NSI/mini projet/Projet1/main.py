# Importation des modules et fonctions
import fct_deezer
import fct_spotify


# Convertiseur de Spotify a Deezer

def Spotify_to_deezer():
    # Connexion aux comptes
    sp = fct_spotify.connexion_spotify()
    dz, client = fct_deezer.connexion_deezer()
    
    # Recuperation de la playlist sur Spotify
    a_convertir = fct_spotify.recuperation_playliste_spotify(sp)
    
    # Creation et convertion sur deezer
    fct_deezer.creation_playlist(dz,client,a_convertir)
    
# Convertiseur de Deezer a Spotify
def Deezer_to_spotify():
    # Connexion aux comptes
    dz, client = fct_deezer.connexion_deezer()
    sp = fct_spotify.connexion_spotify()
    
    # Recuperation de la playlist sur Deezer
    a_convertir = fct_deezer.recuperation_playlist_deezer(dz,client)

    # Creation et convertion sur spotify
    fct_spotify.creation_playlist(sp,a_convertir)



while True:
    a = input()