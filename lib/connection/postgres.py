'''Sqllite Connection Class'''
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
import psycopg2

class PostgresConnection:
    '''Sqlalchemy Connection Class to generate Postgres sessions'''

    def __init__(self, config: dict):
        '''Initilization method for connection class
        
        :param config: dict of postgres config options
        '''
        self.db_type = 'postgres'
        self.name = f"://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['db_name']}"
        self.engine = create_engine(f"postgresql+psycopg2{self.name}", pool_pre_ping=True)
        self.create_database()
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.session_factory)

    def create_database(self)->None:
        '''Checks if database exists and creates database

        :return: None
        '''
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

    @contextmanager
    def session_scope(self) -> scoped_session:
        '''Provide a scoped session to perform operations on sqllite db
        
        :returns: scoped sqllite session
        '''
        session = self.session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

