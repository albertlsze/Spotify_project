import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship


class MusicKeyDB():

    def __init__(self):
        self.name = 'musickeydb'
        self.meta = MetaData()
        self.table = Table(self.name, self.meta,
                           Column('music_key', Integer,primary_key=True),
                           Column('music_note', String(5)),
                           )

    def create_table(self,connection):
        engine = connection.engine
        if not engine.dialect.has_table(engine, self.name):
            self.table.create(engine)
        else:
            print(self.name, 'database already exists')