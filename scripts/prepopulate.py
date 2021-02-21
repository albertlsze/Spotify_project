from config.database_config import sql_config
from lib.models.declarative_base import DeclarativeBase
from lib.connection.mysql import MYSQLConnection
from lib.schemas.musickeydb import MusicKeySchema
from lib.schemas.artistdb import ArtistSchema
from lib.schemas.genredb import GenreSchema
from lib.schemas.songdb import SongSchema
from lib.schemas.yeardb import YearSchema
import lib.utils.Data_pipeline.prepopulate_db as prepopulate

SQL_cnx = MYSQLConnection(sql_config)
sql_tables = {
    'musickey': MusicKeySchema(),
    'genre' : GenreSchema(),
    'artist' : ArtistSchema(),
    'song' : SongSchema(),
    'year' : YearSchema()
}

DeclarativeBase.metadata.drop_all(SQL_cnx.engine)
DeclarativeBase.metadata.create_all(SQL_cnx.engine)

'''
print('\n')
prepopulate.prepopulate_musicdb(SQL_cnx, sql_tables['musickey'])
#prepopulate.prepopulate_yeardb(SQL_cnx, sql_tables['year'])

SQL_cnx.close()
'''