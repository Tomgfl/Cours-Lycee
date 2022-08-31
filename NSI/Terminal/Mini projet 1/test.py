import spotipy
from spotipy.oauth2 import SpotifyOAuth


#ID pour la connexion a l'API de spotify
s_client_id = '3a17d9f8c1014f198c91d214ec31aa07'
s_client_secret = '0b4f9e9ef27e485db92beeaf75d47f0a'   
s_redirect_url='https://google.fr'

def connexion_spotify():
    '''Connexion au compte Spotify'''

    
    print('Vous allez etre regiriger vers spotify pour vous connecter a votre compte\nPuis colle le lien vers lequel vous avez ete rediriger.\n')
    a = input('Appuyer sur "Entrer" pour continuer.')

    
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(s_client_id, s_client_secret, s_redirect_url, scope=scope))
    return sp









