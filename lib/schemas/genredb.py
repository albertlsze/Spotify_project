import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, MetaData


class GenreDB():

    def __init__(self):
        self.meta = MetaData()
        self.table = Table('test', self.meta,
                           Column('genres',String(100),primary_key=True),
                           Column('acousticness_mean', Float),
                           Column('danceability_mean', Float),
                           Column('duration_ms_mean', Float),
                           Column('energy_mean', Float),
                           Column('instrumentalness_mean', Float),
                           Column('liveness_mean', Float),
                           Column('loudness_mean', Float),
                           Column('speechiness_mean', Float),
                           Column('tempo_mean', Float),
                           Column('valence_mean', Float),
                           Column('popularity_mean', Float),
                           Column('music_key_mode', Integer),
                           Column('major_minor_mode', Integer),
                           )

    def create_table(self,connection):
        self.table.create(connection.engine)