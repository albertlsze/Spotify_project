import pandas as pd
from lib.connection.mysql import MYSQLConnection
from lib.models.yeardb import YearDB
from lib.models.musickeydb import MusicKeyDB

def add_pd_to_sql(pd_df:pd,cnx:MYSQLConnection, db_obj) -> None:
    try:
        pd_df.to_sql(db_obj.name, cnx.connection, if_exists='append');
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Table %s created successfully." % db_obj.name);

def create_table(cnx:MYSQLConnection, db_obj) -> None:
    db_obj.create_table(cnx.connection)

def  prepopulate_musicdb(cnx:MYSQLConnection, table:MusicKeyDB) -> None:
    musickey_data = "../lib/utils/Data_pipeline/Prepopulated_data/music_key.csv"
    musickey_data = pd.read_csv(musickey_data)

    musickey_data.set_index('music_key', inplace=True)

    add_pd_to_sql(musickey_data,cnx,table)

def prepopulate_yeardb(cnx:MYSQLConnection, table:YearDB) -> None:
    year_data = "../lib/utils/Data_pipeline/Prepopulated_data/data_by_year.csv"
    year_data = pd.read_csv(year_data)

    col_name = []
    for i in year_data.columns:
        if 'year' in i:
            col_name.append('release_year')
        elif 'key' in i:
            col_name.append('music_key_mode')
        elif 'mode' in i:
            col_name.append('major_minor_mode')
        else:
            col_name.append(i + '_mean')
    year_data.columns = col_name
    year_data.set_index('release_year', inplace=True)

    add_pd_to_sql(year_data,cnx,table)