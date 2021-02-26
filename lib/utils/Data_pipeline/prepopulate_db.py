import pandas as pd
from lib.connection.mysqlcnx import MYSQLConnection
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

def  prepopulate_db(cnx:MYSQLConnection, table:dict) -> None:
    table['musickey']['obj'].load_csv("./Prepopulated_data/music_key.csv")
    table['genre']['obj'].load_csv("./Prepopulated_data/data_by_genres.csv")
    table['year']['obj'].load_csv("./Prepopulated_data/data_by_year.csv")
    table['artist']['obj'].load_csv("./Prepopulated_data/data_by_artist_preprocessed.csv")
    table['song']['obj'].load_csv("./Prepopulated_data/song_data.csv")

    for key in table:
        print('\n',key)
        add_pd_to_sql(table[key]['obj'].data,cnx,table[key]['obj'])