from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = "user_info"

    user_info_id = Column("user_info_id", Integer, primary_key=True)
    name = Column("name", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    administrator = Column("administrator", Boolean)

    def __init__(self, name, password, administrator):
        self.name = name
        self.password = password
        self.administrator = administrator


connection_string = "mysql+mysqlconnector://b3fzksidqav8cwc13x8a:pscale_pw_x0l8zGXZn9RDaB1YvNDwT21qe9XkFS3akOVg0uFqMDB@aws.connect.psdb.cloud:3306/cartaamiga"
engine = create_engine(connection_string, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user_info = UserInfo("admin", "admin",True)
session.add(user_info)
session.commit()
