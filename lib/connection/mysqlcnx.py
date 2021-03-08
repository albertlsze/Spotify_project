import pymysql
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class MYSQLConnection:
    ''' MYSQL connection class to connect to MYSQL server'''

    def __init__(self, config: dict) -> None:
        ''' Initialize connection to MYSQL database

        param:
        - config: dictionary of mysql configurations
        '''

        #self.engine = create_engine('mysql+pymysql://'+config['username']+':'+config['password']+'@'+config['host']+'/'+config['database'])
        self.engine = create_engine(f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}/{config['database']}")
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.session_factory)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()