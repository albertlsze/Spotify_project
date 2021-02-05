import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, MetaData


class ArtistDB():

    def __init__(self):
        self.name = 'artistdb'
        self.meta = MetaData()
        self.table = Table('artistdb', self.meta,
                           Column('artists_id', String(100), primary_key=True),
                           Column('artists',String(100)),
                           Column('artist_popularity', Integer),
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
                           Column('num_tracks', Integer),
                           Column('genre', String(100)),
                           Column('followers', Integer, default=0),
                           )

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name, 'database already exists')