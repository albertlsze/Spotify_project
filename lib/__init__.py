'''Shared Objects to be used by all relevant scripts'''
from lib.schemas import ArtistSchema, GenreSchema, MusicKeySchema, SongSchema, YearSchema
from .connection.mysqlcnx import MYSQLConnection
from config.database_config import sql_config

SQL_cnx = MYSQLConnection(sql_config)
'''ARTIST_SCHEMA = ArtistSchema()
MANY_ARTIST_SCHEMA = ArtistSchema(many=True)
GENRE_SCHEMA = GenreSchema()
MANY_GENRE_SCHEMA = GenreSchema(many=True)
MUSICKEY_SCHEMA = MusicKeySchema()
MANY_MUSICKEY_SCHEMA = MusicKeySchema(many=True)
'''
SONG_SCHEMA = SongSchema()
MANY_SONG_SCHEMA = SongSchema(many=True)
'''YEAR_SCHEMA = YearSchema()
MANY_YEAR_SCHEMA = YearSchema(many=True)
'''