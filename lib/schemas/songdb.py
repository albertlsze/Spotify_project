import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Date, MetaData


class SongDB():

    def __init__(self):
        self.name = 'sonddb'
        self.meta = MetaData()
        self.table = Table('songdb', self.meta,
                           Column('song_id', String(100), primary_key=True),
                           Column('song_name', String(100)),
                           Column('artists_id', String(1000)),
                           Column('acousticness', Float),
                           Column('danceability', Float),
                           Column('duration_ms', Integer),
                           Column('energy', Float),
                           Column('explicit', Boolean),
                           Column('instrumentalness', Float),
                           Column('liveness', Float),
                           Column('loudness', Float),
                           Column('speechiness', Float),
                           Column('tempo', Float),
                           Column('valence', Float),
                           Column('popularity', Integer),
                           Column('music_key', Integer),
                           Column('major_minor', Boolean),
                           Column('release_date', Date),
                           )

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name, 'database already exists')