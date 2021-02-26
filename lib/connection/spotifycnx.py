from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

class SpoyifyConnection:
    ''' Spotify connection class to connect to Spotify API'''

    def __init__(self, config: dict) -> None:
        ''' Initialize connection to MYSQL database

        param:
        - config: dictionary of mysql configurations
        '''
        self.engine = SpotifyClientCredentials(client_id=config['client_id'], client_secret=config['client_secret'])
        self.scope = spotipy.Spotify(client_credentials_manager=self.engine)