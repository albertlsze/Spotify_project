import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase
import pandas as pd
from pprint import pprint

class SongDB(DeclarativeBase):
    __tablename__ = 'songdb'
    song_id = Column(String(100), primary_key=True)
    song_name = Column(String(1000))
    artists_id = Column(String(1000))
    acousticness = Column(Float)
    danceability = Column(Float)
    duration_ms = Column(Integer)
    energy = Column(Float)
    explicit = Column(Integer)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    loudness = Column(Float)
    speechiness = Column(Float)
    tempo = Column(Float)
    valence = Column(Float)
    popularity = Column(Integer)
    music_key = Column(Integer, ForeignKey('musickeydb.music_key'))
    major_minor = Column(Boolean)
    release_date = Column(Date)
    year = Column(Integer)
    hit_song = Column(Integer)


    musickey = relationship("MusicKeyDB")

    def __init__(self):
        self.name = 'songdb'

    def load_csv(self,filename):
        self.data = pd.read_csv(filename)
        self.data = self.data.drop(columns=['artists'])
        self.data = self.data[self.data['id'].notnull()]
        self.data = self.data.drop_duplicates(['id'], keep='first')

        col_name = []
        for i in self.data.columns:
            if 'key' in i:
                col_name.append('music_key')
            elif 'mode' in i:
                col_name.append('major_minor')
            elif 'id' == i:
                col_name.append('song_id')
            elif 'name' in i:
                col_name.append('song_name')
            else:
                col_name.append(i)
        self.data.columns = col_name
        self.data.set_index('song_id', inplace=True)