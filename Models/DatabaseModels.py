from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String, Integer, Text, Date
from sqlalchemy.orm import sessionmaker, declarative_base
#from Session import DbSession

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


class Letter(Base):
    __tablename__ = "letter"

    letter_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer)
    date = Column(Date, nullable=False)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)

    def __init__(self, sender_id, receiver_id, date, title, message):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.date = date
        self.title = title
        self.message = message