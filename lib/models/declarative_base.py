from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta

Base = declarative_base()
class DeclarativeBase(Base):
    __abstract__ = True