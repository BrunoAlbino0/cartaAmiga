from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, declarative_base
from Models.Session import DbSession
from Models.DatabaseModels import Letter,UserInfo
import datetime

class Letter_Dao():

    def __init__(self, session):
        self.session = session

    def add_letter(self, sender_id, receiver_id, title, message):
        data = datetime.date.today()
        newLetter = Letter(sender_id, receiver_id, data, title, message)
        self.session.add(newLetter)
        self.session.commit()

    def get_all_letters(self):
        #search = "SELECT letter.letter_id, letter.sender_id, letter.title, user_info.name FROM letter INNER JOIN user_info ON letter.sender_id = user_info.user_info_id"
        search_result = self.session.execute(
            select(Letter.letter_id, Letter.sender_id, Letter.title, Letter.date, Letter.message, UserInfo.name)
            .join(UserInfo, Letter.sender_id == UserInfo.user_info_id)
            .order_by(Letter.date)
        )

        for record in search_result:
            print(record)


