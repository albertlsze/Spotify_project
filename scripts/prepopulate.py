from config.database_config import sql_config
from lib.connection.mysql import MYSQLConnection
from lib.schemas.genredb import GenreDB
from lib.schemas.artistdb import ArtistDB
from lib.schemas.songdb import SongDB
from lib.schemas.yeardb import YearDB

connection = MYSQLConnection(sql_config)

genre = GenreDB()
genre.create_table(connection)

artistdb = ArtistDB()
artistdb.create_table(connection)

songdb = SongDB()
songdb.create_table(connection)

yeardb = YearDB()
yeardb.create_table(connection)