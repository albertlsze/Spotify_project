import pymysql
from sqlalchemy import create_engine

class MYSQLConnection:
    ''' MYSQL connection class to connect to MYSQL server'''

    def __init__(self, config: dict):
        ''' Initialize connection to MYSQL database

        param:
        - config: dictionary of mysql configurations
        '''

        self.cnx = create_engine('mysql+pymysql://'+config['username']+':'+config['password']+'@'+config['host']+'/'+config['database'])
