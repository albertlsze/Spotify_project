'''Functions to populate the musickey database with information'''
from lib.connection.postgres import PostgresConnection
from lib.connection.spotifycnx import SpoyifyConnection
from typing import List, Dict, NoReturn
from lib.resources.Spotipy_API import get_new_releases, get_album_tracks, get_audio_features, get_track_info
from lib.resources.song_timescale_db import MultiTimeTracks
from datetime import datetime
from lib.utils.Data_pipeline.insert_into_databases import (insert_data_into_database,insert_song_times)
from pprint import pprint


def divide_chunks(data:List, n:int):
    # looping till length data
    for i in range(0, len(data), n):
        yield data[i:i + n]

def get_new_release_features(song_ids:List[List], sp_cnx:SpoyifyConnection, *args) -> List[Dict]
    features = []
    for id_50 in song_ids:
        for arg in args:
            features += arg(sp_cnx, id_50)
    return features

def get_song_ids (db_connection:MultiTimeTracks, sp_cnx:SpoyifyConnection, new_releases:List[Dict])->List[List]:
    song_ids = db_connection.get_distinct_items_ids()
    for album in new_releases:
        new_tracks = get_album_tracks(sp_cnx,album['id'])

        for track in new_tracks:
            song_ids.add(track['id'])
    song_ids = list(divide_chunks(list(song_ids), 50))
    return song_ids

def get_new_releases_track_infos(song_ids:List[List], sp_cnx:SpoyifyConnection):
    track_infos = []
    for id_50 in song_ids:
        track_infos += get_track_info(sp_cnx, id_50)
    return track_infos

def populate_new_releases(sql_cnx:PostgresConnection, sp_cnx:SpoyifyConnection):
    '''

    :param sql_cnx:
    :param sp_cnx:
    :return:
    '''
    print('---------------------------------------------')
    print('Daily update of New Releases')
    print('---------------------------------------------')
    #print(f'update time: {last_update}')
    print('querying New Releases for Spotify API')

    db_connection = MultiTimeTracks()
    new_releases = get_new_releases(sp_cnx)
    song_ids = get_song_ids (db_connection, sp_cnx, new_releases)
    track_infos = get_new_releases_track_infos(song_ids, sp_cnx)


    new_releases = []
    date = str(datetime.now().date())

    for track in track_infos:
        temp = {'date': date,
                'song_id': track['id'],
                'song_name': track['name'],
                'artists_id': '',
                'release_date': track['album']['release_date']
                }
        for artist_info in track['artists']:
            temp['artists_id'] += f"{artist_info['id'],}"
        temp['artists_id'] = temp['artists_id'][:-1]

        if 'popularity' in track:
            temp['popularity'] = track['popularity']

        new_releases.append(temp)



    print('Loading into Database')
    insert_data_into_database(new_releases, insert_song_times)
    print('---------------------------------------------')

    song_id = Column(String(100), primary_key=True)
    song_name = Column(String(1000))
    artists_id = Column(String(1000))
    acousticness = Column(Float)
    danceability = Column(Float)
    duration_ms = Column(Integer)
    energy = Column(Float)
    explicit = Column(Integer)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    loudness = Column(Float)
    speechiness = Column(Float)
    tempo = Column(Float)
    valence = Column(Float)
    popularity = Column(Integer)
    music_key = Column(Integer, ForeignKey('musickeydb.music_key'))
    major_minor = Column(Boolean)
    release_date = Column(Date)
    year = Column(Integer)
    hit_song = Column(Integer)
