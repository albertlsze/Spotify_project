from lib import SQL_cnx, sp_cnx
from lib.utils.Data_pipeline.get_new_releases import populate_new_releases

if __name__ == '__main__':
    populate_new_releases(SQL_cnx,sp_cnx)