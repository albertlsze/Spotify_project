import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase

class GenreDB(DeclarativeBase):
    __tablename__ = 'genredb'
    genres = Column(String(100), primary_key=True)
    acousticness_mean = Column(Float)
    danceability_mean = Column(Float)
    duration_ms_mean = Column(Float)
    energy_mean = Column(Float)
    instrumentalness_mean = Column(Float)
    liveness_mean = Column(Float)
    loudness_mean = Column(Float)
    speechiness_mean = Column(Float)
    tempo_mean = Column(Float)
    valence_mean = Column(Float)
    popularity_mean = Column(Float)
    music_key_mode = Column(Integer, ForeignKey('musickeydb.music_key'))
    major_minor_mode = Column(Integer)
    musickey = relationship("MusicKeyDB")

    def __init__(self):
        self.name = 'genredb'
        #self.meta = MetaData()

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name,'database already exists')