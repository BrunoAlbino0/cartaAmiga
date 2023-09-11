from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = "user_info"

    user_info_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    administrator = Column(Boolean)

    def __init__(self, name, password, administrator):
        self.name = name
        self.password = password
        self.administrator = administrator


