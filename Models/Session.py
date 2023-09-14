from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()
import os

class DbSession:
    connection_string =os.getenv("DATABASE_CONNECTION")

    def __init__(self):
        self.engine = create_engine(self.connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.dbsession = self.Session()
