'''Shared Objects to be used by all relevant scripts'''
from lib.schemas import ArtistSchema, GenreSchema, MusicKeySchema, SongSchema, SongTimeSchema, YearSchema
from .connection.mysqlcnx import MYSQLConnection
from .connection.postgres import PostgresConnection
from .connection.spotifycnx import SpoyifyConnection
from config.database_config import sql_config, POSTGRES_CONFIG, spotify_api_config

#SQL_cnx = MYSQLConnection(sql_config)
SQL_cnx = PostgresConnection(POSTGRES_CONFIG)
sp_cnx = SpoyifyConnection(spotify_api_config)
ARTIST_SCHEMA = ArtistSchema()
MANY_ARTIST_SCHEMA = ArtistSchema(many=True)
GENRE_SCHEMA = GenreSchema()
MANY_GENRE_SCHEMA = GenreSchema(many=True)
MUSICKEY_SCHEMA = MusicKeySchema()
MANY_MUSICKEY_SCHEMA = MusicKeySchema(many=True)
SONG_SCHEMA = SongSchema()
MANY_SONG_SCHEMA = SongSchema(many=True)
SONG_TIME_SCHEMA = SongTimeSchema()
MANY_SONG_TIME_SCHEMA = SongTimeSchema(many=True)
YEAR_SCHEMA = YearSchema()
MANY_YEAR_SCHEMA = YearSchema(many=True)

