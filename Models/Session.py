from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbSession:
    connection_string = "mysql+mysqlconnector://b3fzksidqav8cwc13x8a:pscale_pw_x0l8zGXZn9RDaB1YvNDwT21qe9XkFS3akOVg0uFqMDB@aws.connect.psdb.cloud:3306/cartaamiga"

    def __init__(self):
        self.engine = create_engine(self.connection_string, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
