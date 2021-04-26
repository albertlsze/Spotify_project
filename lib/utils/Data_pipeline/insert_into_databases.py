'''Functions to populate the musickey database with information'''
from typing import List, Dict, NoReturn

from lib import (ARTIST_SCHEMA, MANY_ARTIST_SCHEMA,
                 GENRE_SCHEMA, MANY_GENRE_SCHEMA,
                 MUSICKEY_SCHEMA, MANY_MUSICKEY_SCHEMA,
                 SONG_SCHEMA, MANY_SONG_SCHEMA,
                 SONG_TIME_SCHEMA, MANY_SONG_TIME_SCHEMA,
                 YEAR_SCHEMA, MANY_YEAR_SCHEMA
                 )
from lib import SQL_cnx

import datetime
from pprint import pprint

def insert_data_into_database(item_list: List[Dict],*args) -> NoReturn:
    with SQL_cnx.session() as sess:
        for arg in args:
            item_objs = arg(item_list,sess)
            sess.bulk_save_objects(item_objs, update_changed_only=False)

def insert_artists(item_list: List[Dict], sess):
    '''Insert artist data into database.

    :param item_list: artist data
    :return: MANY_ARTIST_SCHEMA
    '''
    return MANY_ARTIST_SCHEMA.load(item_list, session=sess)

def insert_genres(item_list: List[Dict], sess):
    '''Insert genre data into database.

    :param item_list: genre data
    :return: MANY_GENRE_SCHEMA
    '''
    return MANY_GENRE_SCHEMA.load(item_list, session=sess)

def insert_musickeys(item_list: List[Dict], sess):
    '''Insert Musickey data into database.

    :param item_list: musickey data
    :return: MANY_MUSICKEY_SCHEMA
    '''
    return MANY_MUSICKEY_SCHEMA.load(item_list, session=sess)

def insert_songs(item_list: List[Dict], sess):
    '''Insert song data into database.

    :param item_list: song data
    :return: MANY_SONG_SCHEMA
    '''
    return MANY_SONG_SCHEMA.load(item_list, session=sess)

def insert_song_times(item_list: List[Dict], sess):
    '''Insert song_time data into database.

    :param item_list: song_time data
    :return: MANY_SONG_TIME_SCHEMA
    '''
    return MANY_SONG_TIME_SCHEMA.load(item_list, session=sess)

def insert_years(item_list: List[Dict], sess):
    '''Insert year data into database.

    :param item_list: year data
    :return: MANY_YEAR_SCHEMA
    '''
    return MANY_YEAR_SCHEMA.load(item_list, session=sess)