import pandas as pd
from lib.connection.mysql import MYSQLConnection
from lib.models.yeardb import YearDB
from lib.models.musickeydb import MusicKeyDB

def add_pd_to_sql(pd_df:pd,cnx:MYSQLConnection, db_obj) -> None:
    try:
        pd_df.to_sql(db_obj.name, cnx.engine, if_exists='append');
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Table %s created successfully." % db_obj.name);

def  prepopulate_musicdb(cnx:MYSQLConnection, table:MusicKeyDB) -> None:
    table.load_csv("../lib/utils/Data_pipeline/Prepopulated_data/music_key.csv")

    add_pd_to_sql(table.data,cnx,table)

def prepopulate_yeardb(cnx:MYSQLConnection, table:YearDB) -> None:
    table.load_csv("../lib/utils/Data_pipeline/Prepopulated_data/data_by_year.csv")

    add_pd_to_sql(year_data,cnx,table)