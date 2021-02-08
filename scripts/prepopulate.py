from config.database_config import sql_config
from lib.connection.mysql import MYSQLConnection
from lib.schemas.yeardb import YearDB
from lib.schemas.genredb import GenreDB
from lib.schemas.artistdb import ArtistDB
from lib.schemas.songdb import SongDB
from lib.schemas.musickeydb import MusicKeyDB
import lib.utils.Data_pipeline.prepopulate_db as prepopulate
import os

SQL_cnx = MYSQLConnection(sql_config)
sql_tables = {
    'musickey': MusicKeyDB(),
    'genre' : GenreDB(),
    'artist' : ArtistDB(),
    'song' : SongDB(),
    'year' : YearDB()
}

for key in sql_tables:
    prepopulate.create_table(SQL_cnx,sql_tables[key])

print('\n')
prepopulate.prepopulate_musicdb(SQL_cnx, sql_tables['musickey'])
#prepopulate.prepopulate_yeardb(SQL_cnx, sql_tables['year'])

SQL_cnx.close()