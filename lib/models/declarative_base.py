from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta

class PostfixerMeta(DeclarativeMeta):
    '''Declarative Meta class to append env to
    table names'''
    def __init__(cls, name, bases, dict_):
        if '__tablename__' in dict_:
            cls.__tablename__ = dict_['__tablename__']

        super().__init__(name, bases, dict_)

Base = declarative_base(metaclass=PostfixerMeta)

class DeclarativeBase(Base):
    '''
        Create Declarative base for SQL connection
    '''
    __abstract__ = True