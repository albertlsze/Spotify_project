import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData


class ArtistDB():

    def __init__(self):
        meta = MetaData()
        self.table = Table('test', meta,
                           Column()
                           Column('employee_id', Integer, primary_key=True),
                           Column('employee_name', String(60), nullable=False, key='name'),
                           Column('employee_dept', Integer, ForeignKey("departments.department_id"))
                           )
        employees.create(engine)