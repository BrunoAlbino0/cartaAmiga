from Models.Session import DbSession
from Models.User_Info_Dao import User_Info_Dao


class Model:

    def __init__(self):
        self.user_logged = False
        self.user_id = 0
        self.session = DbSession()
        self.user_info_dao = User_Info_Dao(self.session.session)

    def user_info_search_by_id(self, user_id):
        print("Recebi no modelo: " + user_id)
        self.user_info_dao.user_info_search_by_id(user_id)


    def user_info_search_by_name(self, user_name):
        print("Recebi no modelo: " + user_name)
        self.user_info_dao.user_info_search_by_name(user_name)
