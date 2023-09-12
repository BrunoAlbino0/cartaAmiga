from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, declarative_base
from Models.Session import DbSession
from Models.DatabaseModels import Letter
import datetime

class Letter_Dao():

    def __init__(self, session):
        self.session = session

    def add_letter(self, sender_id, receiver_id, title, message):
        data = datetime.date.today()
        newLetter = Letter(sender_id, receiver_id, data, title, message)
        self.session.add(newLetter)
        self.session.commit()
