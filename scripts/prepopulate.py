from config.database_config import sql_config
from lib.models.declarative_base import DeclarativeBase
from lib.connection.mysqlcnx import MYSQLConnection
from lib.schemas.musickeydb import MusicKeySchema
from lib.schemas.artistdb import ArtistSchema
from lib.schemas.genredb import GenreSchema
from lib.schemas.songdb import SongSchema
from lib.schemas.yeardb import YearSchema
from lib.models.musickeydb import MusicKeyDB
from lib.models.genredb import GenreDB
from lib.models.artistdb import ArtistDB
from lib.models.songdb import SongDB
from lib.models.yeardb import YearDB
import lib.utils.Data_pipeline.prepopulate_db as prepopulate

SQL_cnx = MYSQLConnection(sql_config)
sql_tables = {
    'musickey': {'schema':MusicKeySchema(),'obj':MusicKeyDB()},
    'genre' : {'schema':GenreSchema(),'obj':GenreDB()},
    'artist' : {'schema':ArtistSchema(),'obj':ArtistDB()},
    'song' : {'schema':SongSchema(),'obj':SongDB()},
    'year' : {'schema':YearSchema(),'obj':YearDB()}
}

DeclarativeBase.metadata.drop_all(SQL_cnx.engine)
DeclarativeBase.metadata.create_all(SQL_cnx.engine)

prepopulate.prepopulate_db(SQL_cnx, sql_tables)
'''
print('\n')
prepopulate.prepopulate_musicdb(SQL_cnx, sql_tables['musickey'])
#prepopulate.prepopulate_yeardb(SQL_cnx, sql_tables['year'])

SQL_cnx.close()
'''