from config.database_config import sql_config
from lib.connection.mysql import MYSQLConnection
from lib.schemas.genredb import GenreDB

connection = MYSQLConnection(sql_config)
genre = GenreDB()
genre.create_table(connection)
