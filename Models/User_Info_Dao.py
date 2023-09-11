from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from Models.Session import DbSession
from Models.DatabaseModels import UserInfo

class User_Info_Dao():

    def __init__(self, Session):
        self.session = Session

    def user_info_search_by_id(self, user_id):
        #search_result = self.session.select(UserInfo).where(UserInfo.user_info_id == user_id)
        search_result = self.session.query(UserInfo).all()
        print(search_result)

    def user_info_search_by_name(self, user_name):
        #search_result = self.session.select(UserInfo).where(UserInfo.name == user_name)
        search_result = self.session.query(UserInfo).all()
        print(search_result)
