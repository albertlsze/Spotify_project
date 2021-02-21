import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase
import pandas as pd

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

    def load_csv(self, filename):
        self.data = pd.read_csv(filename)

        col_name = []
        for i in self.data.columns:
            if 'genres' in i:
                continue
            elif 'key' in i:
                col_name.append('music_key_mode')
            elif 'mode' in i:
                col_name.append('major_minor_mode')
            else:
                col_name.append(i + '_mean')
        self.data.columns = col_name
        self.data.set_index('genres', inplace=True)