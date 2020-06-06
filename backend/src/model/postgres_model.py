import logging
import psycopg2
from src.config.config import DB_HOST,DB_PORT,DB_PWD,DATABASE,DB_USER

logger = logging.getLogger(__name__)


class DbConnection:
    def __init__(self):
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.database = DATABASE
        self.user = DB_USER
        self.password = DB_PWD

    def create_db_connection(self):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.db_host,
                               port=self.db_port)
        logger.info('Database connection successful')
        return conn

    def apply_data(self, statement):
        connection = self.create_db_connection()
        cur = connection.cursor()
        cur.execute(statement)
        connection.commit()
        logger.info('Query executed successfully')

