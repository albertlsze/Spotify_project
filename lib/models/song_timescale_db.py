import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, Boolean, Date, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase
import pandas as pd
from pprint import pprint

class SongTimeDB(DeclarativeBase):
    '''
        Create Song time table structure using SQLalchemy and timescaledb
    '''
    __tablename__ = 'songtimedb'
    __table_args__ = (
        Index('date_idx', 'date'),
    )

    date = Column(Date, primary_key=True)
    song_id = Column(String(100), ForeignKey('songdb.song_id') , primary_key=True)
    song_name = Column(String(1000), primary_key=True)
    artists_id = Column(String(1000), primary_key=True)
    popularity = Column(Integer)
    release_date = Column(Date)

    song = relationship("SongDB")