import sqlalchemy
from typing import NoReturn
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Index
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase
import pandas as pd
from pprint import pprint

class ArtistDB(DeclarativeBase):
    '''
        Create Artist table structure using SQLalchemy
    '''
    __tablename__ = 'artistdb'
    __table_args__ = (
        Index('artists_id_idx','artists_id'),
    )

    artists_id = Column(String(100), primary_key=True)
    artists = Column(String(1000), primary_key=True)
    artist_popularity = Column(Integer)
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
    num_tracks = Column(Integer)
    genre = Column(String(1000))
    followers = Column(Integer, default=0)
    musickey = relationship("MusicKeyDB")

    def load_csv(self, filename:str)->NoReturn:
        '''
            load any preexisting csv data file and preprocess the data, by changing column names

        :param filename: file path of csv data
        :return: None
        '''
        self.data = pd.read_csv(filename)
        self.data = self.data[self.data['artists_id'].notnull()]
        self.data = self.data.drop_duplicates(['artists_id'],keep='first')

        skip = {'genre','followers','artists','artists_id','artist_popularity'}
        col_name = []
        for i in self.data.columns:
            if i in skip:
                col_name.append(i)
            elif 'key' in i:
                col_name.append('music_key_mode')
            elif 'mode' in i:
                col_name.append('major_minor_mode')
            elif 'count' in i:
                col_name.append('num_tracks')
            else:
                col_name.append(i + '_mean')
        self.data.columns = col_name
        #self.data.set_index('artists_id', inplace=True)
        self.data = self.data.where(pd.notnull(self.data), None)
        self.data = self.data.to_dict(orient='records')