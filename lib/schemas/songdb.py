import sqlalchemy
from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Date, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase

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
    music_key = Column(Integer, ForeignKey('musickey.music_key'))
    major_minor = Column(Boolean)
    release_date = Column(Date)
    hit_song = Column(Integer)

    def __init__(self):
        self.name = 'songdb'
        #self.meta = MetaData()

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name, 'database already exists')