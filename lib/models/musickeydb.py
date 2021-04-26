import sqlalchemy
from sqlalchemy import Column, Integer, String
from lib.models.declarative_base import DeclarativeBase
import pandas as pd

class MusicKeyDB(DeclarativeBase):
    '''
        Create musickey table structure using SQLalchemy
    '''
    __tablename__ = "musickeydb"
    music_key = Column(Integer, primary_key=True, autoincrement=False)
    music_note = Column(String(5))

    def load_csv(self,filename):
        '''
            load any preexisting csv data file

        :param filename: file path of csv data
        :return: None
        '''
        self.data = pd.read_csv(filename)
        #self.data.set_index('music_key', inplace=True)
        self.data = self.data.where(pd.notnull(self.data), None)
        self.data = self.data.to_dict(orient='records')