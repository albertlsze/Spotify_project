#from .. import sp_cnx
from ..connection.spotifycnx import SpoyifyConnection
from typing import Dict, List

def new_releases(sp_cnx:SpoyifyConnection)->List[Dict]:

    response = sp_cnx.scope.new_releases()
    new_releases = []
    while response:
        albums = response['albums']
        new_releases += albums['items']

        if albums['next']:
            response = sp_cnx.scope.next(albums)
        else:
            response = None
    return new_releases

def get_album_tracks(sp_cnx:SpoyifyConnection,album_id)->List[Dict]:
    tracks = sp_cnx.scope.album_tracks(album_id)
    album_tracks = []

    while tracks:
        album_tracks += tracks['items']

        if tracks['next']:
            tracks = sp_cnx.scope.next(tracks)
        else:
            tracks = None
    return album_tracks

def get_track(sp_cnx:SpoyifyConnection,track_ids:List[str])->List[Dict]:
    tracks = sp_cnx.scope.tracks(track_ids)
    return tracks['tracks']

def get_audio_features(sp_cnx:SpoyifyConnection,track_ids:List[str])->List[Dict]:
    audio_feature = sp_cnx.scope.audio_features(track_ids)
    return audio_feature

