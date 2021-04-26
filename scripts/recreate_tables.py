from lib import SQL_cnx
from lib.models.declarative_base import DeclarativeBase
from lib.schemas.musickeydb import MusicKeySchema
from lib.schemas.artistdb import ArtistSchema
from lib.schemas.genredb import GenreSchema
from lib.schemas.songdb import SongSchema
from lib.schemas.song_timecale_db import SongTimeSchema
from lib.schemas.yeardb import YearSchema
from lib.models.musickeydb import MusicKeyDB
from lib.models.genredb import GenreDB
from lib.models.artistdb import ArtistDB
from lib.models.songdb import SongDB
from lib.models.yeardb import YearDB
from lib.models.song_timescale_db import SongTimeDB
from sqlalchemy.sql import text

#SQL_cnx = MYSQLConnection(sql_config)
#SQL_cnx = PostgresConnection(POSTGRES_CONFIG)
sql_tables = {
    'musickey': {'schema':MusicKeySchema(),'obj':MusicKeyDB()},
    'genre' : {'schema':GenreSchema(),'obj':GenreDB()},
    'artist' : {'schema':ArtistSchema(),'obj':ArtistDB()},
    'song' : {'schema':SongSchema(),'obj':SongDB()},
    'year' : {'schema':YearSchema(),'obj':YearDB()},
    'songtime' : {'schema':SongTimeSchema(),'obj':SongTimeDB()}
}

DeclarativeBase.metadata.drop_all(SQL_cnx.engine)
DeclarativeBase.metadata.create_all(SQL_cnx.engine)

connect = SQL_cnx.engine.connect()
sql_comand = text("SELECT create_hypertable('songtimedb', 'date')")

result = connect.execute(sql_comand)