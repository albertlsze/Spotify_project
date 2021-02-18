import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from lib.models.declarative_base import DeclarativeBase

class MusicKeyDB(DeclarativeBase):
    __tablename__ = "musickeydb"
    music_key = Column(Integer, primary_key=True)
    music_note = Column(String(5))

    def __init__(self):
        self.name = 'musickeydb'

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name, 'database already exists')