import sqlalchemy
from sqlalchemy import Column, Integer, String
from lib.models.declarative_base import DeclarativeBase
import pandas as pd

class MusicKeyDB(DeclarativeBase):
    __tablename__ = "musickeydb"
    music_key = Column(Integer, primary_key=True)
    music_note = Column(String(5))

    def __init__(self):
        self.name = 'musickeydb'

    def load_csv(self,filename):
        self.data = pd.read_csv(filename)
        self.data.set_index('music_key', inplace=True)