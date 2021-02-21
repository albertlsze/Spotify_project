import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase
import pandas as pd

class SongDB(DeclarativeBase):
    __tablename__ = 'songdb'
    song_id = Column(String(100), primary_key=True)
    song_name = Column(String(100))
    artists_id = Column(String(1000))
    acousticness = Column(Float)
    danceability = Column(Float)
    duration_ms = Column(Integer)
    energy = Column(Float)
    explicit = Column(Boolean)
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
    hit_song = Column(Integer)

    musickey = relationship("MusicKeyDB")

    def __init__(self):
        self.name = 'songdb'

    def load_csv(self,filename):
        self.data = pd.read_csv(filename)