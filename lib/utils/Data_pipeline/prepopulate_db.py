import pandas as pd
#from lib.connection.mysqlcnx import MYSQLConnection
from lib.connection.postgres import PostgresConnection
from lib.models.yeardb import YearDB
from lib.models.musickeydb import MusicKeyDB
from lib.utils.Data_pipeline.insert_into_databases import (insert_data_into_database,
                                                           insert_artists, insert_genres, insert_musickeys,
                                                           insert_song_times, insert_songs, insert_years
                                                           )

def add_pd_to_sql(pd_df:pd,cnx:PostgresConnection, db_obj) -> None:
    ''' adds data from a panda dataframe into sql database

    :param pd_df: data in a pandas data frame
    :param cnx: SQL connection
    :param db_obj: type of database model
    :return: None
    '''
    try:
        pd_df.to_sql(db_obj.name, cnx.engine, if_exists='append');
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Table %s created successfully." % db_obj.name);

def  prepopulate_db(cnx:PostgresConnection, table:dict) -> None:
    '''Prepopulates sql databases with preexisting data

    :param cnx: SQL connection
    :param table: dictionary with all database models
    :return: None
    '''
    table['musickey']['obj'].load_csv("./Prepopulated_data/music_key.csv")
    table['genre']['obj'].load_csv("./Prepopulated_data/data_by_genres.csv")
    table['year']['obj'].load_csv("./Prepopulated_data/data_by_year.csv")
    table['artist']['obj'].load_csv("./Prepopulated_data/data_by_artist_preprocessed.csv")
    table['song']['obj'].load_csv("./Prepopulated_data/song_data.csv")



    for key in table:
        if hasattr(table[key]['obj'], 'data'):
            print(key)
            #add_pd_to_sql(table[key]['obj'].data,cnx,table[key]['obj'])
            insert_data_into_database(table[key]['obj'].data,eval(f"insert_{key}s"))